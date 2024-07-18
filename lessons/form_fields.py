from typing import Optional, List

from fastapi import FastAPI, Form

app = FastAPI()


# 导入 Form
# 创建表单（Form）参数的方式与 Body 和 Query 一样
#
# 提示
# 声明表单体要显式使用 Form ，否则，FastAPI 会把该参数当作查询参数或请求体（JSON）参数
@app.post("/login/")
async def login(username: str = Form(...), password: str = Form(...)):
    return {"username": username}


# 关于 "表单字段"
# 技术细节
#
# 表单数据的「媒体类型」编码一般为 application/x-www-form-urlencoded。
#
# 但包含文件的表单编码为 multipart/form-data
@app.post("/items/")
async def create_item(
    name: str = Form(...),
    description: str = Form(None),
    price: float = Form(...),
    tax: Optional[float] = Form(None),
    tags: List[str] = Form(...),
):
    return {
        "name": name,
        "description": description,
        "price": price,
        "tax": tax,
        "tags": tags,
    }
