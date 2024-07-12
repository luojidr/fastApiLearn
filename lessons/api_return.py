from pydantic import BaseModel
from runserver import app


@app.get("/return_int")
def return_int():
    return 123456


@app.get("/return_str")
def return_str():
    return "QAZXSW"


@app.get("/return_float")
def return_float():
    return 12.346


@app.get("/return_list")
def return_list():
    return [1, 2, 3, 4, 5]


@app.get("/return_dict")
def return_dict():
    return dict(name="derek", ages=35)


@app.get("/return_pydantic")
def return_pydantic():
    class User(BaseModel):
        name: str
        age: int
    return User(**dict(name="derek", age=35))
