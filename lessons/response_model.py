"""
响应模型
"""
from typing import List, Optional

from fastapi import FastAPI
from pydantic import BaseModel, EmailStr, Field

app = FastAPI()


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None
    tags: List[str] = []


# 响应模型 response_model 是作为get、post等方法(路径操作装饰器)的参数，用于指定响应的模型类型；他不像其他框架Django或Flask一样，是作为一个独立的响应类。
# 不像之前的所有参数和请求体，它不属于路径操作函数。
#
# 技术细节
# 响应模型在参数中被声明，而不是作为函数返回类型的注解，这是因为路径函数可能不会真正返回该响应模型，而是返回一个 dict、数据库对象或其他模型，
# 然后再使用 response_model 来执行字段约束和序列化。
@app.post("/items/", response_model=Item)
async def create_item(item: Item):
    return item


class UserIn(BaseModel):
    username: str
    password: str
    email: EmailStr
    full_name: Optional[str] = None


# Don't do this in production!
@app.post("/user/", response_model=UserIn)
async def create_user(user: UserIn):
    return user


# 添加输出模型
class UserOut(BaseModel):
    username: str
    email: EmailStr
    full_name: Optional[str] = None


@app.post("/user/", response_model=UserOut)
async def create_user(user: UserIn):
    return user


# 响应模型编码参数
# response_model_exclude_unset 参数: 响应中将不会包含那些默认值，而是仅有实际设置的值, 哪怕实际设置的值为空
# response_model_exclude_defaults 参数: 响应中将不会包含那些默认值，如果实际设置的值与默认值一样也不会包括
# response_model_exclude_none 参数: 响应中将不会包含那些值为 None 的字段，不论是默认值还是实际设置的值，只要为None就不会包括
# response_model_include 参数: 响应中只包含指定的字段，而不是全部字段
#   如果你忘记使用 set 而是使用 list 或 tuple，FastAPI 仍会将其转换为 set 并且正常工作
# response_model_exclude 参数: 响应中不包含指定的字段
# response_model_by_alias 参数: 响应中包含的是 alias 而不是字段名
class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None
    tags: List[str] = []


items = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "description": "The bartenders", "price": 62, "tax": 20.2},
    "baz": {"name": "Baz", "description": None, "price": 50.2, "tax": 10.5, "tags": []},
}


@app.get(
    "/items/{item_id}",
    response_model=Item,
    # response_model_exclude_unset=True,
    # response_model_exclude_defaults=True,
    # response_model_exclude_none=True,
    response_model_include={"name", "description"},
    # response_model_include=["name", "description"],  # 会转成 set,如果你忘记使用 set 而是使用 list 或 tuple，FastAPI 仍会将其转换为 set 并且正常工作
    response_model_exclude={"tax"},
    # response_model_exclude=["tax"],   # 会转成 set
)
async def read_item(item_id: str):
    return items[item_id]


# response_model_by_alias: 默认为 True, 响应中包含的是 alias 而不是字段名
# 只要使用了 response_model_by_alias参数，那么属兔函数的返回值必须使用 response_model 的字段别名
# 可以理解为响应模型的字段名使用的是 alias 而不是字段名，如下代码所示
class ItemAlias(BaseModel):
    item_id: int = Field(..., alias='id')
    item_name: str = Field(..., alias='name')


@app.get("/items/alias/{item_id}", response_model=ItemAlias, response_model_by_alias=False)
async def read_item_alias(item_id: int):
    # response_model_by_alias 为 True, return 值必须是符合 response_model 的字段的别名，如果是字段名则会报错
    # return {"id": item_id, "name": "Item Name"} # 响应结果 {"id": 1, "name": "Item Name"}

    # response_model_by_alias 为 False, return 必须使用 response_model 的字段别名
    return {"id": item_id, "name": "Item Name"}  # Ok
    # return {"item_id": item_id, "item_name": "Item Name"}  # Error
