from enum import Enum
from pydantic import BaseModel
from runserver import app


@app.get("/items/{item_id}")
def read_item(item_id):
    return {"item_id": item_id}


@app.get("/items/{item_id}")
def read_item_int(item_id: int):
    # 注意：上面的路径会接收到所有的 /items/123f, /items/123 的请求，需要把他放到后面，否则会拦截所有的请求
    # 因为上面的请求路径覆盖了本请求的所有请求，请求不会被这个路径匹配到到
    # 如果参数item_id不是 int 类型，会报错
    # {
    #     "detail": [
    #         {
    #             "type": "int_parsing",
    #             "loc": ["path", "item_id"],
    #             "msg":"Input should be a valid integer, unable to parse string as an integer",
    #             "input": "123f"
    #         }
    #     ]
    # }
    return {"item_id_int": item_id}


# 预设值， 希望预先设定可能的有效参数值，使用 Enum
class ModelName(str, Enum):
    """ 字符擦的枚举 """
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    """
    获取模型
    【注意】：路径中的model_name ，必须是ModelName枚举类型的其中一个，如果不是，会报错
    :param model_name:
    :return:
    """
    print(type(model_name), model_name.value)

    # 注意：在返回值中 model_name 是框架帮我们转成了字符串，帮我们省了很多事；在一般的开发中，我们使用model_name.value 来获取对应的字符串值
    if model_name == ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}


# 路径转换器
@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}

