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
load_dotenv("secure.env", override=True)  # overlay secrets
BASE_URL = os.getenv("CONFLUENCE_BASE_URL", "https://genesys-confluence.atlassian.net")
EMAIL    = os.getenv("ATLASSIAN_EMAIL")
TOKEN    = os.getenv("ATLASSIAN_TOKEN")
SPACES   = os.getenv("CONFLUENCE_SPACES", "PureCloud").split(",")  # comma‑list
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
    """Fast export of a Confluence space using the v2 API.

    Changes vs. previous version
    ───────────────────────────
    • **Parallel page‑body fetch** with ThreadPoolExecutor (8 workers)
    • **Removed duplicate‑version check** to avoid extra disk I/O
    • Keeps filename truncation + rich .meta output
    """
    # 1️⃣ Resolve key → id
    resp = session.get(
        f"{BASE_URL}/wiki/api/v2/spaces",
        params={"keys": space_key},
        timeout=30,
    )
    resp.raise_for_status()
    results = resp.json().get("results", [])
    if not results:
        log.error("Space key '%s' not found or insufficient permissions", space_key)
        return 0
    space_id = results[0]["id"]
    log.info("Resolved space '%s' → id %s", space_key, space_id)

    # 2️⃣ Iterate pages (follow _links.next)
    from concurrent.futures import ThreadPoolExecutor, as_completed

    page_url: str = f"{BASE_URL}/wiki/api/v2/spaces/{space_id}/pages"
    params: dict = {"limit": 200}
    total: int = 0

    def fetch_full(pid: str):
        return conf.get_page_by_id(
            pid,
            expand="body.storage,version,ancestors,metadata.labels,history",
        )

    while True:
        log.info("GET %s", page_url)
        r = session.get(page_url, params=params, timeout=30)
        r.raise_for_status()
        data = r.json()

        page_map = {item["id"]: item.get("title", f"page-{item['id']}") for item in data.get("results", [])}
        if not page_map:
            break

        # 8‑way parallel fetch of bodies
        with ThreadPoolExecutor(max_workers=8) as pool:
            futures = {pool.submit(fetch_full, pid): pid for pid in page_map}
            for fut in as_completed(futures):
                full = fut.result()
                page_id = futures[fut]
                title = page_map[page_id]

                storage = (full.get("body") or {}).get("storage") or {} # type: ignore
                html = storage.get("value", "")
                if not html:
                    continue

                # Metadata
                ver = full.get("version", {}).get("number", "unknown") # type: ignore
                updated = full.get("version", {}).get("when", "") # type: ignore
                author = (full.get("version", {}).get("by") or {}).get("displayName", "") # type: ignore
                anc_titles = [a.get("title", "") for a in full.get("ancestors", [])] # type: ignore
                path = " / ".join(anc_titles + [title])
                labels = ",".join(l.get("name", "") for l in (full.get("metadata", {}).get("labels", {}).get("results", []))) # type: ignore
                url = f"{BASE_URL.rstrip('/')}{full.get('_links', {}).get('webui', '')}" # type: ignore

                slug = slugify(title)[:180]
                fname = OUT_DIR / f"{slug}.md"
                meta_path = OUT_DIR / f"{slug}.meta"

                # Write files (overwrite is okay – faster than reading first)
                md = h2m.handle(html)
                fname.write_text(md, encoding="utf-8")
                meta_path.write_text(
                    f"id: {page_id}\n"
                    f"space: {space_key}\n"
                    f"version: {ver}\n"
                    f"updated: {updated}\n"
                    f"author: {author}\n"
                    f"path: {path}\n"
                    f"url: {url}\n"
                    f"labels: {labels}\n"
                )
                total += 1

        next_rel = (data.get("_links") or {}).get("next")
        if not next_rel:
            break
        page_url = f"{BASE_URL.rstrip('/')}{next_rel}"
        params = {}

    log.info("Space '%s' – wrote %s pages", space_key, total)
    return total


t0 = time.perf_counter()
total_pages = 0
for key in [k.strip() for k in SPACES if k.strip()]:
    log.info("Pulling space '%s' …", key)
    total_pages += export_space(key)

duration = time.perf_counter() - t0
log.info("✅ Downloaded %s pages into %s in %.1fs", total_pages, OUT_DIR, duration)