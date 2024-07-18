from typing import List

from fastapi.responses import HTMLResponse
from fastapi import FastAPI, File, UploadFile

app = FastAPI()


# 導入 File
# 必須使用 File 函數才能獲取文件數據
# File: 讀取的是文件的内容
@app.post("/files/")
async def create_file(file: bytes = File(...)):
    return {"file_size": len(file)}


# 说明
# File 是直接继承自 Form 的类。
# 注意，从 fastapi 导入的 Query、Path、File 等项，实际上是返回特定类的函数。
#
# 提示
# 声明文件体必须使用 File，否则，FastAPI 会把该参数当作查询参数或请求体（JSON）参数。
# 文件作为「表单数据」上传。
# 如果把路径操作函数参数的类型声明为 bytes，FastAPI 将以 bytes 形式读取和接收文件内容。
# 这种方式把文件的所有内容都存储在内存里，适用于小型文件。
# 不过，很多情况下，UploadFile 更好用。
# 【注意】：UploadFile 与 bytes 相比有更多优势：
# 使用 spooled 文件：存储在内存的文件超出最大上限时，FastAPI 会把文件存入磁盘
# 这种方式更适于处理图像、视频、二进制文件等大型文件，好处是不会占用所有内存
# 可获取上传文件的元数据
# 自带 file-like async 接口
# 暴露的 Python SpooledTemporaryFile 对象，可直接传递给其他预期「file-like」对象的库
#
# UploadFile 的属性如下:
# filename：上传文件名字符串（str），例如， myimage.jpg
# content_type：内容类型（MIME 类型 / 媒体类型）字符串（str），例如， image/jpeg
# file：file-like 对象，可直接传递给其他预期「file-like」对象的库.
#   SpooledTemporaryFile（ file-like 对象）。其实就是 Python文件，可直接传递给其他预期 file-like 对象的函数或支持库。
#
# UploadFile 支持以下 async 方法，（使用内部 SpooledTemporaryFile）可调用相应的文件方法。
# write(data)：把 data （str 或 bytes）写入文件；
# read(size)：按指定数量的字节或字符（size (int)）读取文件内容；
# seek(offset)：移动至文件 offset （int）字节处的位置；例如，await myfile.seek(0) 移动到文件开头；执行 await myfile.read() 后，需再次读取已读取内容时，这种方法特别好用；
# close()：关闭文件。
#
@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):
    print(file)
    content = await file.read()
    print(content)
    return {"filename": file.filename}


# 多文件上传
# FastAPI 支持同时上传多个文件。
# 可用同一个「表单字段」发送含多个文件的「表单数据」。
# 上传多个文件时，要声明含 bytes 或 UploadFile 的列表（List）
@app.post("/multi-files/")
async def create_multiple_files(files: List[bytes] = File(...)):
    return {"file_sizes": [len(file) for file in files]}


@app.post("/multi-uploadfile/")
async def create_multiple_upload_files(files: List[UploadFile] = File(...)):
    return {"filenames": [file.filename for file in files]}


@app.get("/html/")
async def main():
    content = """
        <body>
        <form action="/multi-files/" enctype="multipart/form-data" method="post">
        <input name="files" type="file" multiple>
        <input type="submit">
        </form>
        <form action="/multi-uploadfile/" enctype="multipart/form-data" method="post">
        <input name="files" type="file" multiple>
        <input type="submit">
        </form>
        </body>
    """
    return HTMLResponse(content=content)



if __name__ == "__main__":
    import uvicorn

    uvicorn.run("lessons.upload_files:app", host="127.0.0.1", port=8000, reload=True, workers=1)
