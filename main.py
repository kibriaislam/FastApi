from typing import Optional
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def main():
    return {"message": "Hello World!!"}


@app.get("/item/{item_id}")
def read_item(item_id: int , q: Optional[str] = None):
    return {"item_id": item_id , "q": q}