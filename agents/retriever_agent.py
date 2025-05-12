from fastapi import APIRouter
from langchain.vectorstores import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.document_loaders import TextLoader

router = APIRouter()
loader = TextLoader("data_ingestion/news.txt")
docs = loader.load()
embeddings = OpenAIEmbeddings()
vectorstore = FAISS.from_documents(docs, embeddings)

@router.get("/retrieve")
def retrieve_info(query: str):
    docs = vectorstore.similarity_search(query, k=3)
    return [doc.page_content for doc in docs]
