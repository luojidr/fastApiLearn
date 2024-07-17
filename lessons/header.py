from typing import Optional, List

from fastapi import FastAPI, Header

app = FastAPI()


# 导入 Header 和 声明 Header 参数
# 和Path, Query and Cookie 一样的结构定义 header 参数
# 第一个值是默认值，你可以传递所有的额外验证或注释参数
# 注意：
# 大多数标准的headers用 "连字符" 分隔，也称为 "减号" (-)。
# 但是像 user-agent 这样的变量在Python中是无效的。
# 因此, 默认情况下, Header 将把参数名称的字符从下划线 (_) 转换为连字符 (-) 来提取并记录 headers.
# 同时，HTTP headers 是大小写不敏感的，因此，因此可以使用标准Python样式(也称为 "snake_case")声明它们。
# 因此，您可以像通常在Python代码中那样使用 user_agent ，而不需要将首字母大写为 User_Agent 或类似的东西
@app.get("/items/")
async def read_items(
    user_agent: Optional[str] = Header(None),
):
    return {"User-Agent": user_agent}


# 重复的 headers
# Header 函数中有个 convert_underscores  参数，表示是否将下划线转换为连字符，默认为 True；为 False , 则将下划线转换为连字符
# convert_underscores=True,  curl -X 'GET' -H "x-token:123" -H "x-token:456" http://127.0.0.1:8000/items2/
#       如果头的key写成：x_token 不起作用
# convert_underscores=False,  curl -X 'GET' -H "x_token:123" -H "x_token:456" http://127.0.0.1:8000/items2/
#       如果头的key写成：x-token 不起作用
@app.get("/items2/")
async def read_items2(
    x_token: Optional[List[str]] = Header(None, convert_underscores=False)
):
    return {"X-Token values": x_token}
