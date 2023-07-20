from typing import Optional
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from search import searchPaper
from chat import summarize, polish

app = FastAPI()
app.add_middleware(
	CORSMiddleware,
	allow_origins=["http://localhost:8080"],
    allow_methods=["GET", "POST"],
    allow_headers=["Content-Type"],
    allow_credentials=True,
)

class paperInfo:
    title: str
    author: str
    detail: str
    pdf:str
    categories: str

    def __init__(self,title,author,id,categories):
        self.title = title
        self.author = author
        if(id != None):
            self.detail = f'https://arxiv.org/abs/{id}'
            self.pdf = f'https://arxiv.org/pdf/{id}'
        else:
            self.detail = "unknown"
            self.pdf = "unknown"
        self.categories = categories


@app.get("/search/{query}")
def get_paper(query: str):
    abstract, info = searchPaper(polish(query))
    answer = summarize(query,abstract)
    papers = []
    for i in info:
        papers.append(paperInfo(i.get("title"),i.get("author"),i.get("acess_id"),i.get("categories")))
    return {
        "answer": answer,
        "paperInfo": papers
    }

@app.get("/hello")
def sayhi():
    return {
        "message":"hello"
    }
