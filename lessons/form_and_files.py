from typing import Annotated, List

from fastapi import FastAPI, File, Form, UploadFile

app = FastAPI()


# FastAPI 支持同时使用 File 和 Form 定义文件和表单字段（web框架都支持，不是fastapi獨有）
# 接收上传文件或表单数据，要预先安装 python-multipart。
@app.post("/files/")
async def create_file(
        file: bytes = File(...),            # 請求體表單字段 file
        fileb: UploadFile = File(...),      # 請求體表單字段 fileb
        token: str = Form(...),             # 請求體表單字段 token
):
    return {
        "file_size": len(file),
        "token": token,
        "fileb_content_type": fileb.content_type,
    }


if __name__ == '__main__':
    import uvicorn

    uvicorn.run("lessons.form_and_files:app", host="127.0.0.1", port=8000, reload=True)
