import time
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Milvus

def searchPaper(query):
    time.sleep(10)
    embedding = HuggingFaceEmbeddings()
    time.sleep(10)
    db = Milvus(embedding_function=embedding, collection_name="arXiv_prompt",connection_args={"host": "172.29.4.47", "port": "19530"})
    time.sleep(10)

    search_result = db.search(query, search_type="similarity")
    
    abstract = [doc.page_content for doc in search_result]
    info = [doc.metadata for doc in search_result]
    return abstract, info
