from typing import Optional, Set

from fastapi import FastAPI, status
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None
    tags: Set[str] = []


# 几个参数传递给路径操作装饰器(不是路径操作函数)
# response_model: 指定响应体模型(前面講過)
# status_code: 指定响应状态码, eg: status.HTTP_201_CREATED
# tags: 指定响应标签(這樣將接口分類，在OpenAPI文檔中清晰分明)
# summary: 指定api摘要(在OpenAPI文檔中)
# description: 指定api描述(在OpenAPI文檔中)
# 文档字符串的描述(函数 docstring 中声明路径操作描述)
# response_description: 指定响应描述(肯定是在Responses裏面了)
# deprecated: 指定是否已弃用(将路径操作标记为deprecated，但不删除它)
@app.post(
    "/items/",
    response_model=Item,
    status_code=status.HTTP_201_CREATED,
    summary="Create an item",
    description="Create an item with all the information, name, description, price, tax and a set of unique tags",
    tags=["items"],
    response_description="The created item very nice!",
    deprecated=True,
)
async def create_item(item: Item):
    """ docstring 如下：
       Create an item with all the information:

       - **name**: each item must have a name
       - **description**: a long description
       - **price**: required
       - **tax**: if the item doesn't have tax, you can omit this
       - **tags**: a set of unique tag strings for this item
   """
    return item


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)



