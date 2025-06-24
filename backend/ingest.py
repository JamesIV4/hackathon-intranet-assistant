from pathlib import Path
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
import os

DATA_DIR = Path(__file__).resolve().parent.parent / "data"
DB_PATH = Path(__file__).parent / "faiss_index"

emb = HuggingFaceEmbeddings(model_name=os.getenv("EMBEDDING_MODEL"))

docs = []
for md in DATA_DIR.rglob("*.md"):
    pages = TextLoader(str(md)).load()
    docs.extend(pages)

splitter = RecursiveCharacterTextSplitter(chunk_size=800, chunk_overlap=120)
chunks = splitter.split_documents(docs)

faiss_db = FAISS.from_documents(chunks, emb)
faiss_db.save_local(DB_PATH) # type: ignore
print("✅ Ingestion complete →", DB_PATH)
