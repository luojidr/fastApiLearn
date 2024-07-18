"""
JSON兼容编码器
在某些情况下，您可能需要转换数据类型（如Pydantic模型），将其转换为与JSON兼容的数据结构（如dict，list等）,請使用 jsonable_encoder 函数
"""
from datetime import datetime
from typing import Optional

from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel, Field

fake_db = {}


class Item(BaseModel):
    title: str
    timestamp: datetime
    description: Optional[str] = None

    class Config:
        json_encoders = {
            datetime: lambda v: v.strftime("%Y-%m-%d %H:%M:%S"),  # 指定格式
        }


app = FastAPI()


# 在此示例中，它将 Pydantic 模型转换为一个字典，并将这个datetime转换为一个字符串
# jsonable_encoder 將 Item 對象實例轉化爲一個字典，將 datetime 轉化爲一個字符串(默認ISO 格式："2024-07-18T08:10:59.169Z")
@app.put("/items/{id}")
def update_item(id: str, item: Item):
    json_compatible_item_data = jsonable_encoder(item)
    fake_db[id] = json_compatible_item_data
    return fake_db[id]


# 对于 datetime 也可以不用 class Config 方式来指定类型，通过下面的方式也可以：
class MyDateTime(datetime):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, value):
        if isinstance(value, datetime):
            return value
        return datetime.fromisoformat(value)

    def __str__(self):
        return self.strftime('%Y-%m-%d %H:%M:%S')  # 自定义格式


class MyItem(BaseModel):
    title: str
    timestamp: MyDateTime = Field(default_factory=datetime.now)
    description: Optional[str] = None


@app.put("/items/my")
def update_item(item: Item):
    # response: {
    #     "title": "string",
    #     "timestamp": "2024-07-18 08:25:57",
    #     "description": "string"
    # }
    return jsonable_encoder(item)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
