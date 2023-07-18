from typing import Optional
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI

app = FastAPI()
app.add_middleware(
	CORSMiddleware,
	allow_origins=["http://localhost:8080"],
    allow_methods=["GET", "POST"],
    allow_headers=["Content-Type"],
    allow_credentials=True,
)

@app.get("/")
def read_root():
    return {"content": "Hello World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}