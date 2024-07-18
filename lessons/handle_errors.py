from fastapi import FastAPI, Query
from fastapi import status
from fastapi.encoders import jsonable_encoder
from fastapi import HTTPException
from fastapi.exceptions import RequestValidationError, WebSocketRequestValidationError
from fastapi.requests import Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel

app = FastAPI()

items = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "price": 62, "description": "The bartenders"},
    "baz": {"name": "Baz", "price": 50.2, "description": "There goes my baz"},
}


# 錯誤響應信息：
# {
#   "detail": "Item not found"
# }
@app.get("/items/{item_id}")
async def read_item(item_id: str):
    if item_id not in items:
        # raise ValueError("Item not found")  # 框架不會返回錯誤的信息，直接在程序裏報錯

        # 触发 HTTPException 时，可以用参数 detail 传递任何能转换为 JSON 的值，不仅限于 str。
        # 还支持传递 dict、list 等数据结构。FastAPI 能自动处理这些数据，并将之转换为 JSON
        raise HTTPException(status_code=404, detail="Item not found")  # 框架會返回錯誤的信息
    return items[item_id]


# 添加自定义响应头
@app.get("/items-header/{item_id}")
async def read_item_header(item_id: str):
    if item_id not in items:
        raise HTTPException(
            status_code=404,
            detail="Item not found",
            headers={"X-Error": "There goes my baz"}  # Response headers
        )
    return items[item_id]


# 安装自定义异常处理器
class UnicornException(Exception):
    def __init__(self, name: str):
        self.name = name


# app.exception_handler 每次只能注冊一種異常，如果想要一次注冊多個一場可在實例化app時候傳入 exception_handlers 參數， 用法如下：
# async def not_found(request: Request, exc: HTTPException):
#     return HTMLResponse(content=HTML_404_PAGE, status_code=exc.status_code)
#
# async def server_error(request: Request, exc: HTTPException):
#     return HTMLResponse(content=HTML_500_PAGE, status_code=exc.status_code)
#
# exception_handlers = {
#     404: not_found,
#     500: server_error
# }
# app = FastAPI(exception_handlers=exception_handlers)
@app.exception_handler(UnicornException)
async def unicorn_exception_handler(request: Request, exc: UnicornException):
    # 參數格式：request 與 異常類的二個參數
    return JSONResponse(
        status_code=418,
        content={"message": f"Oops! {exc.name} did something. There goes a rainbow..."},
    )


@app.get("/unicorns/{name}")
async def read_unicorn(name: str):
    if name == "yolo":
        raise UnicornException(name=name)
    return {"unicorn_name": name}


# 覆盖默认异常处理器
@app.get("/default-errors/")
async def read_default_errors(q: int = Query(...)):
    if q == 1:
        raise HTTPException(status_code=501, detail="覆盖默认异常处理器:HTTPException")

    if q == 2:
        # 響應結果： {"detail": [{"loc": ["query", "q"], "msg": "q is 2", "type": "value_error"}]}
        raise RequestValidationError(errors=[{"loc": ["query", "q"], "msg": "q is 2", "type": "value_error"}],)

    if q == 3:
        raise WebSocketRequestValidationError(errors=[{"loc": ["query", "q"], "msg": "q is 3", "type": "value_error"}],)


# 使用 RequestValidationError 的请求体
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder({"detail": exc.errors(), "body": exc.body})
    )


class Item(BaseModel):
    title: str
    size: int


@app.post("/items/")
async def create_item(item: Item):
    # 如果參數類型不正確(如size)，會返回如下的錯誤響應
    # {
    #     "detail": [
    #         {
    #             "type": "int_parsing",
    #             "loc": [
    #                 "body",
    #                 "size"
    #             ],
    #             "msg": "Input should be a valid integer, unable to parse string as an integer",
    #             "input": "dkfj"
    #         }
    #     ],
    #     "body": {
    #         "title": "ewewf",
    #         "size": "dkfj"
    #     }
    # }
    return item


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
