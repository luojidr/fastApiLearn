"""
笔记:
    PATCH 没有 PUT 知名，也怎么不常用。
    很多人甚至只用 PUT 实现部分更新。
    FastAPI 对此没有任何限制，可以随意互换使用这两种操作。
"""
from typing import List, Optional

from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    tax: float = 10.5
    tags: List[str] = []


items = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "description": "The bartenders", "price": 62, "tax": 20.2},
    "baz": {"name": "Baz", "description": None, "price": 50.2, "tax": 10.5, "tags": []},
}


@app.get("/items/{item_id}", response_model=Item)
async def read_item(item_id: str):
    return items[item_id]


@app.patch("/items/{item_id}", response_model=Item)
async def update_item(item_id: str, item: Item):
    stored_item_data = items[item_id]
    stored_item_model = Item(**stored_item_data)
    print(f"stored_item_model: {stored_item_model}")
    update_data = item.dict(exclude_unset=True)
    print(f"update_data: {update_data}")
    updated_item = stored_item_model.copy(update=update_data)  # 更新 update_data 中的数据
    print(f"updated_item: {updated_item}")
    items[item_id] = jsonable_encoder(updated_item)
    return updated_item


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)

