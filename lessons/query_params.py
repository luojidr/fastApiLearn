from typing import Optional, Union

from runserver import app


@app.get("/items/")
async def read_items(q: Optional[str] = None, skip: int = 0, limit: int = 10):
    """
    如果 skip 或 limit 不是数字，则返回报错信息
    :param skip:
    :param limit:
    :param q:
    :return:
    """
    print(q, type(q))
    # q: Optional[str] = None  # 等于 Union[str, None], 也是建议的写法
    # q: str = None
    # q: Union[str, None] = None
    # 这三种表示基本相同
    return [{"name": "Foo", "price": 42}]


@app.get("/items/bool/{item_id}")
async def read_item_bool(item_id: str, q: Optional[str] = None, short: bool = False):
    """
    如果 item_id 不是数字，则返回报错信息
    :param item_id:
    :param q:
    :param short: 【注意】，查询参数 short=1, True, true, on, yes 都会认为是为真; off, 0, false, False, no 为假，其他值会报错
    :return:
    """
    item = {"item_id": item_id, "short": short}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing itemthat has a long description"}
        )
    return item
