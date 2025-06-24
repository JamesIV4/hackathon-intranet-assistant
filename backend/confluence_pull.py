#!/usr/bin/env python
"""
confluence_pull.py
──────────────────
Pull every page in one or more Confluence spaces, convert each page’s
XHTML storage body to Markdown, and save into ./data as .md files ready
for ingest.py.

Now with **verbose logging, retry/back‑off, and progress bars** so you
can see exactly what the script is doing.
"""
from __future__ import annotations

import os, re, sys, time, logging
from pathlib import Path

import html2text
import requests
import tqdm
from atlassian import Confluence
from dotenv import load_dotenv
from requests.adapters import HTTPAdapter, Retry

###############################################################################
# Configuration — edit ENV vars rather than this file when possible
###############################################################################
load_dotenv()
BASE_URL = os.getenv("CONFLUENCE_BASE_URL", "https://genesys-confluence.atlassian.net")
EMAIL    = os.getenv("ATLASSIAN_EMAIL")
TOKEN    = os.getenv("ATLASSIAN_TOKEN")
SPACES   = ["PureCloud"]
OUT_DIR  = Path(__file__).resolve().parent.parent / "data"
OUT_DIR.mkdir(exist_ok=True)

###############################################################################
# Logging setup
###############################################################################
logging.basicConfig(
    level=logging.INFO,
    format="[%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)],
)
log = logging.getLogger(__name__)

###############################################################################
# Confluence REST client with retry & timeout
###############################################################################

session = requests.Session()
retries = Retry(total=5, backoff_factor=1.2, status_forcelist=[502, 503, 504])
session.mount("https://", HTTPAdapter(max_retries=retries))

conf = Confluence(
    url=BASE_URL,
    username=EMAIL,
    password=TOKEN,
    cloud=True,
    session=session,
)

###############################################################################
# Helpers
###############################################################################

def slugify(title: str) -> str:
    """Create a safe filename from a Confluence page title."""
    return re.sub(r"[^A-Za-z0-9_\- ]", "-", title).strip().replace(" ", "-")

h2m = html2text.HTML2Text()
h2m.body_width = 0  # preserve wrapping

###############################################################################
# Main export loop
###############################################################################

def export_space(space_key: str) -> int:
    """Export a single space by `space_key` using Confluence **v2** API.

    v2 requires the **numeric** space ID for nested endpoints, so we:
      1. Resolve `space_key` → `space_id` via /spaces?keys=…
      2. Page through `/spaces/{id}/pages` (200 per page max).
      3. For every page, pull full storage body → Markdown.
    """
    # Step 1 – resolve key → id
    r = session.get(f"{BASE_URL}/wiki/api/v2/spaces", params={"keys": space_key}, timeout=30)
    if r.status_code == 404 or not r.json().get("results"):
        log.error("Space key '%s' not found or you lack permission", space_key)
        return 0
    space_id = r.json()["results"][0]["id"]
    log.info("Resolved space '%s' → id %s", space_key, space_id)

    # Step 2 – page through content
    page_url = f"{BASE_URL}/wiki/api/v2/spaces/{space_id}/pages"
    params   = {"limit": 200}
    count    = 0

    while True:
        log.info("GET %s", page_url)
        resp = session.get(page_url, params=params, timeout=30)
        resp.raise_for_status()
        data = resp.json()

        for item in data.get("results", []):
            page_id = item["id"]
            title   = item.get("title", f"page-{page_id}")

            # get body.storage & version in one call (expand)
            full = conf.get_page_by_id(page_id, expand="body.storage,version")
            storage = (full.get("body") or {}).get("storage") or {} # type: ignore
            html = storage.get("value", "")
            if not html:
                continue

            md   = h2m.handle(html)
            fname = OUT_DIR / f"{slugify(title)}.md"
            fname.write_text(md, encoding="utf-8")

            meta  = OUT_DIR / f"{fname.stem}.meta"
            ver   = full.get("version", {}).get("number", "unknown") # type: ignore
            meta.write_text(
                f"id: {page_id}\\n"
                f"space: {space_key}\\n"
                f"version: {ver}\\n"
            )
            count += 1

        next_cursor = data.get("cursor")
        if not next_cursor:
            break
        params = {"cursor": next_cursor, "limit": 200}

    log.info("Space '%s' – wrote %s pages", space_key, count)
    return count


t0 = time.perf_counter()
total_pages = 0
for key in [k.strip() for k in SPACES if k.strip()]:
    log.info("Pulling space '%s' …", key)
    total_pages += export_space(key)

duration = time.perf_counter() - t0
log.info("✅ Downloaded %s pages into %s in %.1fs", total_pages, OUT_DIR, duration)