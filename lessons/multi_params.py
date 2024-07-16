import logging
from typing import Optional, List

from fastapi import FastAPI, Query, Path, Body
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


class User(BaseModel):
    username: str
    full_name: Optional[str] = None


# 混合使用 Path、Query 和请求体参数
# 视图函数中参数 * 表示之前的参数是位置参数，之后的参数是关键字参数，* 作为位置参数和关键字参数的位置
# 此时有二个请求体（item, user），它的请求体如下(和Body中没有embed=True一样)：
#     {
#       "item": {
#         "name": "item_name",
#         "description": "item_description",
#         "price": 10.5,
#         "tax": 2.5
#       },
#       "user": {
#         "username": "user_name",
#         "full_name": "user_full_name"
#       }
#     }
@app.put("/items/{item_id}")
async def update_item(
    *,
    item_id: int = Path(..., title="The ID of the item to get", ge=0, le=1000),     # 路径参数
    q: Optional[str] = Query(None, alias="item-query"),                             # 查询参数
    item: Optional[Item] = None,                                                    # 请求体参数
    user: User,                                                                     # 请求体参数
):
    results = {"item_id": item_id, "user": user}
    if q:
        results.update({"q": q})
    if item:
        results.update({"item": item})
    return results


# 此时只有一个user的请求体，它的请求体如下：
#     {
#       "username": "user_name",
#       "full_name": "user_full_name"
#     }
@app.put("/items2/{item_id}")
async def update_item2(
    *,
    item_id: int = Path(..., title="The ID of the item to get", ge=0, le=1000),     # 路径参数
    q: Optional[str] = Query(None, alias="item-query"),                             # 查询参数
    user: User,                                                                     # 请求体参数
):
    results = {"item_id": item_id, "user": user}
    if q:
        results.update({"q": q})


# 嵌入单个或多个请求体参数
# embed=True 表示该参数实际上是一个具有键名的字典, 请求体是一个活多个参数都一样如下格式。
# 如果多个请求体参数，加不加embed=True，请求体格式一样。
# 此時请求体如下：
#     {
#       "item": {
#         "name": "string",
#         "description": "string",
#         "price": 0,
#         "tax": 0
#       },
#       "user": {
#         "username": "string",
#         "full_name": "string"
#       }
#     }
@app.put("/items3/{item_id}")
async def update_item3(
    *,
    item_id: int = Path(..., title="The ID of the item to get", ge=0, le=1000),     # 路径参数
    q: Optional[str] = Query(None, alias="item-query"),                             # 查询参数
    item: Item = Body(..., embed=True),                                             # 请求体参数
    user: User = Body(..., embed=True),                                             # 请求体参数
):
    results = {"item_id": item_id, "item": item, "user": user}
    print(item, type(item))
    if q:
        results.update({"q": q})

    return results


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
