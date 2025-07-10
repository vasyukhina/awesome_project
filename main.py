from typing import Union

from fastapi import FastAPI

from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float 
    is_offer: Union[bool, None] = None


@app.get("/")
def read_root():
    return {"Hello, World!"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.post("/item/")
def create_item(item: Item):
    return {"name": item.name, "price": item.price}


@app.put("/item/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}


@app.delete("/item/{item_id}")
def delete_item(item_id: int):
    return {"message": f"Item {item_id} deleted"}