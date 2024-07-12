
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    # 可以返回 dict、list，str、int，Pydantic 模型
    # return {"message": "Hello World"}
    # return 1001
    return "hahah"


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


from lessons.api_return import *
from lessons.path_params import *
from lessons.query_params import *


if __name__ == "__main__":
    import uvicorn

    # uvicorn.run(app, host="0.0.0.0", port=8080)  # ok

    # 这里运行时，使用reload=True，在脚本中不能热更新，但在命令行中就可以
    # uvicorn runserver:app --port 8080 --reload  --log-level trace [ --log-level=trace]
    uvicorn.run(app="runserver:app", host="0.0.0.0", port=8080, reload=True)
