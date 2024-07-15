from typing import List, Annotated, get_type_hints
from dataclasses import dataclass

from fastapi import FastAPI, Query
from pydantic import BaseModel, Field

# Annotated:有注释的；带注解的

# 1. 基本用法
# 定义一个带注释的变量
varWithMetadata: Annotated[int, "这是一个附加注释"] = 10
print(varWithMetadata)


# 2. 使用 Annotated 和 pydantic 进行数据验证
class UserModel(BaseModel):
    age: Annotated[int, Field(gt=0, lt=150)]  # 年龄必须在 0 到 150 之间
    name: Annotated[str, Field(min_length=1, max_length=10)]  # 名字长度必须在 1 到 100 之间


user1 = UserModel(age=10, name="John")  # age 只能在(0, 150) 之前， 否则会报错
user2 = UserModel(age=20, name="David")  # name 长度只能在[1, 10] 之前， 否则会报错
print(user1)

# 3. 使用 Annotated 和 FastAPI 生成 API 文档
app: FastAPI = FastAPI()


@app.get("/items/")
async def read_items(
    q: Annotated[str | None, Query(min_length=3, max_length=10)] = None  # q 参数长度必须大于等于 3, 小于等于 10
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


# 4. 自定义元数据
# 自定义元数据类
class Unit:
    def __init__(self, unit: str):
        self.unit = unit


# 使用自定义元数据
Temperature = Annotated[float, Unit("Celsius")]


def set_temperature(temp: Temperature):
    print(f"Setting temperature to {temp} degrees Celsius")


set_temperature(23.5)


# 使用 Annotated 和 dataclass
# dataclass 是Python标准库中的一个装饰器，结合 Annotated，可以为数据类字段添加元数据
@dataclass
class Product:
    name: Annotated[str, "产品名称"]
    price: Annotated[float, "价格，单位为美元"]


product = Product(name="Laptop", price=999.99)
print(product)


#  高级用法：解析 Annotated 注释, 解析 Annotated 注释中的元数据
def func1(
        a: Annotated[List[Annotated[int, "inner integer"]], "outer list"],
        b: Annotated[str, "A string"],
        c: int):
    pass


# 获取函数参数的类型提示
type_hints = get_type_hints(func1)
print(type_hints.items())


# 解析并打印注释
for param, annotation in type_hints.items():
    print("Annotation:", annotation)
    if hasattr(annotation, '__metadata__'):
        print(f"Parameter: {param}, Type: {annotation.__origin__}, Metadata: {annotation.__metadata__}")
