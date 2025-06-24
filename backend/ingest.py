from pathlib import Path
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from dotenv import load_dotenv

load_dotenv()
load_dotenv("secure.env", override=True)  # overlay secrets
from langchain_community.vectorstores import FAISS
import os

DATA_DIR = Path(__file__).resolve().parent.parent / "data"
DB_PATH = Path(__file__).parent / "faiss_index"

model_name = os.getenv("EMBEDDING_MODEL", "all-MiniLM-L6-v2")
emb = HuggingFaceEmbeddings(model_name=model_name)

docs = []
for md in DATA_DIR.rglob("*.md"):
    pages = TextLoader(str(md)).load()
    docs.extend(pages)

if not docs:
    raise ValueError(f"No markdown files found in {DATA_DIR}. Place your wiki .md files there or update the glob pattern.")

splitter = RecursiveCharacterTextSplitter(chunk_size=800, chunk_overlap=120)
chunks = splitter.split_documents(docs)

faiss_db = FAISS.from_documents(chunks, emb)
faiss_db.save_local(str(DB_PATH))
print("✅ Ingestion complete →", DB_PATH)