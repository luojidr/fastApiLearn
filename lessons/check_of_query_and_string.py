from typing import Optional, List
from fastapi import FastAPI, Query

app = FastAPI()


# 查询参数的字符串校验
# 1、Query() 函数接受一个默认值，以及 min_length 和 max_length 参数，用于对查询参数进行长度校验。
# 2、使用 Query 作为默认值，可以在参数上设置默认值，如果参数没有被提供，则使用默认值。这里的默认值为
# 3、q: str = Query(None) 等同于 q: str = None，但是使用 Query 有更多的条件验证。
@app.get("/items/")
async def read_items(
    q: Optional[str] | None = Query(None, min_length=3, max_length=10)
) -> dict:
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


# Query 更多校验
@app.get("/items2/")
async def read_items2(q: Optional[str] = Query(None, min_length=3, max_length=10)):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})

    return results


# Query 正则表达式
@app.get("/items3/")
async def read_items3(
    q: Optional[str] = Query(None, min_length=3, max_length=10, regex="^fixedquery$"), # 等同于 q: Optional[str] = Query("fixedquery", min_length=3),
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})

    return results


# Query 声明为必需参数, Query 的第一个参数 ... , 表示参数是必需的。
@app.get("/items4/")
async def read_items4(q: str = Query(..., min_length=3)):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})

    return results


# Query 查询参数列表 / 多个值
# http://localhost:8000/items/?q=foo&q=bar
# 1、默认是为 None， q: Optional[List[str]] = Query(None)
# 2、其他默认值，    q: Optional[List[str]] = Query(["foo", "bar"])
@app.get("/items5/")
async def read_items5(q: Optional[List[str]] = Query(None)):
    query_items = {"q": q}
    return query_items


# Query 声明更多元数据
# 1、title：标题
# 2、description：描述, OpenAPI | Swagger UI 的接口文档会展示
# 3、alias：别名 可以通过 alias_priority 指定别名的优先级，默认为 0，表示不优先使用别名。
#   http://127.0.0.1:8000/items/?item-query=foobaritems
# 4、弃用参数 deprecated=True
#       现在假设你不再喜欢此参数。
#       你不得不将其保留一段时间，因为有些客户端正在使用它，但你希望文档清楚地将其展示为已弃用。
#       那么将参数 deprecated=True 传入 Query
@app.get("/items6/")
async def read_items6(
    q: Optional[str] = Query(
        None,
        title="hahah",
        description="Query string for the items to search in the database that have a good match",
        min_length=3,
        alias="item-query",
        deprecated=True,
    )
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update( {"q": q})
    return results
