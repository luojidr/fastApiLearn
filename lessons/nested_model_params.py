from typing import Optional, List

from fastapi import FastAPI
from pydantic import BaseModel, HttpUrl


app = FastAPI()


class Image(BaseModel):
    url: HttpUrl
    name: str


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None
    tags: List[str] = []
    images: Optional[List[Image]] = None


class Offer(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    items: List[Item]


# 啰嗦一下，这里只有一个请求体参数 item，那它的格式如下：
# {
#   "name": "Foo",
#   "description": "The pretender",
#   "price": 42.0,
#   "tax": 3.2,
#   "tags": [
#     "rock",
#     "metal"
#   ]
# }
# 如果请求体是二个或二个以上的参数，那么请求体格式如下：
# {
#   "item": {
#     "name": "Foo",
#     "description": "The pretender",
#     "price": 42.0,
#     "tax": 3.2,
#     "tags": [
#       "rock",
#       "metal"
#     ]
#   },
#   "user": {
#     "username": "dave",
#     "full_name": "Dave Grohl"
#   }
# }
@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}
    return results


# 同上，一个请求体参数 offer，那么请求体格式如下：
# {
#     "name": "Foo",
#     "description": "The pretender",
#     "price": 42.0,
#     "tax": 3.2,
#     "tags": [
#         "rock",
#         "metal"
#     ],
#     "items": [
#         {
#             "name": "Foo",
#             "description": "The pretender",
#             "price": 42.0,
#             "tax": 3.2,
#         }
#     ]
# }
@app.post("/offers/")
async def create_offer(offer: Offer):
    return offer
