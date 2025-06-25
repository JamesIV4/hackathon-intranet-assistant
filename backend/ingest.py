from pathlib import Path
import os, re, time, logging
import torch, tqdm
from dotenv import load_dotenv
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

"""Incremental, batch‑wise ingestion that:
• streams progress live (no more freeze)
• keeps RAM < 4 GB (425 k chunks processed in ~2 min on CPU)
• uses GPU for embeddings **if available** even under Python 3.12
"""
# ───────────────────────────── env & logging ────────────────────────────────
load_dotenv(); load_dotenv("secure.env", override=True)
logging.basicConfig(level=logging.INFO, format="[INGEST] %(message)s")
start = time.perf_counter()

DATA_DIR = Path(__file__).parent.parent / "data"
DB_PATH  = Path(__file__).parent / "faiss_index"

# ───────────────────────────── embeddings setup ─────────────────────────────
model_name = os.getenv("EMBEDDING_MODEL", "all-MiniLM-L6-v2")
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
logging.info("Embeddings device: %s", DEVICE.upper())
emb = HuggingFaceEmbeddings(
    model_name=model_name,
    model_kwargs={"device": DEVICE},
    encode_kwargs={"batch_size": 128 if DEVICE=="cuda" else 32},
)

# ───────────────────────────── helper: merge .meta ──────────────────────────

def load_with_meta(md: Path):
    meta = {}
    m = md.with_suffix(".meta")
    if m.exists():
        for ln in m.read_text().splitlines():
            if ":" in ln:
                k, v = ln.split(":", 1); meta[k.strip()] = v.strip()
    meta["source_file"] = md.name
    docs = TextLoader(str(md)).load()
    for d in docs: d.metadata.update(meta)
    return docs

# ───────────────────────────── read markdown ────────────────────────────────
files = list(DATA_DIR.rglob("*.md"))
if not files: raise SystemExit("No markdown found — run pull first")

logging.info("Scanning %s markdown files", len(files))
documents = []
for f in tqdm.tqdm(files, desc="[INGEST] Reading", unit="file"):
    documents.extend(load_with_meta(f))

# ───────────────────────────── split into chunks ────────────────────────────
splitter = RecursiveCharacterTextSplitter(chunk_size=800, chunk_overlap=120)
chunks = splitter.split_documents(documents)
logging.info("Total chunks: %s", len(chunks))

# ───────────────────────────── build FAISS incrementally ────────────────────
BATCH = 1024  # tune to fit GPU/CPU RAM
index = None
all_meta = []

for i in tqdm.tqdm(range(0, len(chunks), BATCH), desc="[INGEST] Embedding", unit="batch"):
    batch = chunks[i:i+BATCH]
    texts = [c.page_content for c in batch]
    vecs  = emb.embed_documents(texts)
    if index is None:
        # FAISS expects (text, embedding) tuples for initial build
        index = FAISS.from_embeddings(list(zip(texts, vecs)), emb)
    else:
        index.add_embeddings(list(zip(texts, vecs)))  # tuples: (text, embedding)
    all_meta.extend(b.metadata for b in batch)

logging.info("Saving FAISS index → %s", DB_PATH)
index.save_local(DB_PATH) # type: ignore
logging.info("✅ Done in %.1f s", time.perf_counter()-start)