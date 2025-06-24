import os, asyncio
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.llms import LlamaCpp
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
from dotenv import load_dotenv

load_dotenv()
load_dotenv("secure.env", override=True)  # overlay secrets
DB_PATH = os.path.join(os.path.dirname(__file__), "faiss_index")

def new_chain():
    emb = HuggingFaceEmbeddings(model_name=os.getenv("EMBEDDING_MODEL"))
    vectordb = FAISS.load_local(DB_PATH, emb, allow_dangerous_deserialization=True)
    retriever = vectordb.as_retriever(search_type="similarity", search_kwargs={"k": 3})
    llm = LlamaCpp(model_path=os.getenv("MODEL_PATH"), n_ctx=4096, n_gpu_layers=0, verbose=False)
    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
    return ConversationalRetrievalChain.from_llm(llm, retriever, memory=memory)

app = FastAPI()

@app.websocket("/ws")
async def chat_ws(ws: WebSocket):
    await ws.accept()
    print("[WS] Connection accepted")
    chain = new_chain()
    try:
        while True:
            data = await ws.receive_text()
            print(f"[WS] Received question: {data}")
            loop = asyncio.get_event_loop()
            result = await loop.run_in_executor(
                None,
                lambda q=data: chain({"question": q})
            )
            answer = result.get("answer", "")
            print(f"[WS] Sending answer: {answer}")
            await ws.send_text(answer)
    except WebSocketDisconnect:
        print("[WS] Client disconnected")
    except Exception as e:
        print(f"[WS] Error: {e}")
        await ws.close()
