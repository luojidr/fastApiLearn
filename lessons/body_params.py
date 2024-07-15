import typing
from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

typing.TYPE_CHECKING = True
app = FastAPI()


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


@app.post("/items/")
async def create_item(item):
    # Item()
    return item


# 请求体 + 路径参数
@app.post("/items2/{item_id}")
async def create_item2(item_id: int, item: Item):
    return {"item_id": item_id, **item.dict()}


@app.post("/items3/{item_id}")
async def create_item3(item_id: int, item: Item, q: Optional[str] = None):
    result = {"item_id": item_id, **item.dict()}
    if q:
        result.update({"q": q})

    return result

# 注意： fastapi 的请求体参数必须使用 json 格式


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
