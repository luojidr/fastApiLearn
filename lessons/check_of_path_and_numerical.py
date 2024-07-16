from typing import Optional, List
from fastapi import FastAPI, Path, Query

app = FastAPI()


# 参数顺序（实际上参数 item_id, q 的顺序哪个在前无所谓，fastapi会自动处理并对应上参数）
@app.get("/items/{item_id}")
async def read_items(
    item_id: int = Path(..., title="The ID of the item to get"),
    q: Optional[str] = Query(None, alias="item-query"),
) -> dict:
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results


# 数值校验
# gt：大于（greater than）
# ge：大于等于（greater than or equal）
# lt：小于（less than）
# le：小于等于（less than or equal）
@app.get("/items2/{item_id}")
async def read_items2(
    item_id: int = Path(..., title="The ID of the item to get", gt=0, le=1000),
    q: Optional[str] = Query(None, alias="item-query"),
) -> dict:
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results




