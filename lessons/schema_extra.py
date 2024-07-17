from typing import Optional

from fastapi import FastAPI, Body
from pydantic import BaseModel, Field

app = FastAPI()


# 在 OpenAPI 文档中【不起】作用（即在OpenAPI 文档中请求体会默认带给定example中的值）
class Item0(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

    class Config:
        schema_extra = {
            "example": {
                "name": "Foo",
                "description": "A very nice Item",
                "price": 35.4,
                "tax": 3.2,
            }
        }


# # 在 OpenAPI 文档中【起】作用
class Item(BaseModel):
    name: str = Field(..., example="Foo")
    description: Optional[str] = Field(None, example="A very nice Item")
    price: float = Field(..., example=35.4)
    tax: Optional[float] = Field(None, example=3.2)


# item 的 example 起作用，item0 的 example不起作用
@app.post("/items/{item_id}")
async def update_item(item_id: int, item: Item, item0: Item0):
    results = {"item_id": item_id, "item": item, "item0": item0}
    return results


# update_item2 写法 item0 的 example 起作用 (Body中的 example 选项)
@app.post("/items2/")
async def update_item2(
        item0: Item = Body(
            ...,
            example={"name": "Foo", "description": "A very nice Item", "price": 35.4, "tax": 3.2}
        )
):
    results = {"item0": item0}
    return results

