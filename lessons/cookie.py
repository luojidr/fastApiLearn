from typing import Optional

from fastapi import Cookie, FastAPI


app = FastAPI()


# 声明 Cookie 参数: 与声明 Query 参数和 Path 参数时相同
# 第一个值是参数的默认值，同时也可以传递所有验证参数或注释参数，来校验参数
# 技术细节
# Cookie 、Path 、Query是兄弟类，它们都继承自公共的 Param 类
# 但请记住，当你从 fastapi 导入的 Query、Path、Cookie 或其他参数声明函数，这些实际上是返回特殊类的函数。
@app.get("/items/")
async def read_items(ads_id: Optional[str] = Cookie(None)):
    return {"ads_id": ads_id}
