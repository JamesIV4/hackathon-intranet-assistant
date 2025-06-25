from pathlib import Path
import os, re
from dotenv import load_dotenv
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

load_dotenv()
load_dotenv("secure.env", override=True)  # overlay secrets

DATA_DIR = Path(__file__).resolve().parent.parent / "data"
DB_PATH  = Path(__file__).parent / "faiss_index"

model_name = os.getenv("EMBEDDING_MODEL", "all-MiniLM-L6-v2")
emb = HuggingFaceEmbeddings(model_name=model_name)

# ──────────────────────────────────────────────────────────────────────────────
# Helper to merge .meta into each Document’s metadata
# ──────────────────────────────────────────────────────────────────────────────

def load_with_meta(md_path: Path):
    """Return a list[Document] for one markdown file, including rich metadata."""
    meta_path = md_path.with_suffix(".meta")
    meta = {}
    if meta_path.exists():
        for line in meta_path.read_text(encoding="utf-8").splitlines():
            if ":" in line:
                k, v = line.split(":", 1)
                meta[k.strip()] = v.strip()
    # Always include filename for traceability
    meta["source_file"] = md_path.name

    docs = TextLoader(str(md_path)).load()  # returns list[Document]
    for d in docs:
        d.metadata.update(meta)
    return docs

# ──────────────────────────────────────────────────────────────────────────────
# Load all markdown + metadata
# ──────────────────────────────────────────────────────────────────────────────

documents = []
for md in DATA_DIR.rglob("*.md"):
    if md.name.startswith("."):
        continue  # skip hidden files
    documents.extend(load_with_meta(md))

if not documents:
    raise ValueError(f"No markdown files found in {DATA_DIR}. Run confluence_pull.py first.")

# ──────────────────────────────────────────────────────────────────────────────
# Chunking + embedding
# ──────────────────────────────────────────────────────────────────────────────

splitter = RecursiveCharacterTextSplitter(chunk_size=800, chunk_overlap=120)
chunks = splitter.split_documents(documents)

faiss_db = FAISS.from_documents(chunks, emb)
faiss_db.save_local(str(DB_PATH))
print("✅ Ingestion complete →", DB_PATH)