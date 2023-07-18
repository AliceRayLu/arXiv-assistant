import time
import sys
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Milvus

time.sleep(10)
embedding = HuggingFaceEmbeddings()
time.sleep(10)
db = Milvus(embedding_function=embedding, collection_name="arXiv_prompt",connection_args={"host": "172.29.4.47", "port": "19530"})
time.sleep(10)

search_result = db.search(sys.argv[1], search_type="similarity")


print(search_result)