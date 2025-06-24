import os, asyncio
from fastapi import FastAPI, WebSocket
from langchain_community.vectorstores import FAISS
from langchain_community.llms import LlamaCpp
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
from dotenv import load_dotenv

load_dotenv()
DB_PATH = os.path.join(os.path.dirname(__file__), "faiss_index")

def new_chain():
    vectordb = FAISS.load_local(DB_PATH, None) # type: ignore
    retriever = vectordb.as_retriever(search_type="similarity", search_kwargs={"k":3})
    llm = LlamaCpp(model_path=os.getenv("MODEL_PATH"), n_ctx=4096, n_gpu_layers=0, verbose=False)
    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
    return ConversationalRetrievalChain.from_llm(llm, retriever, memory=memory)

app = FastAPI()

@app.websocket("/ws")
async def chat_ws(ws: WebSocket):
    await ws.accept()
    chain = new_chain()
    while True:
        data = await ws.receive_text()
        result = await asyncio.get_event_loop().run_in_executor(None, chain, {"question": data})
        await ws.send_text(result["answer"])