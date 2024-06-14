# learning from https://blog.postman.com/how-to-build-an-api-in-python/

from fastapi import FastAPI

app = FastAPI()

static_string = "Initial Text"


@app.get("/get-message")
async def read_root(name: str):
    return {"message": "Congrats, " + name + "! This is your first API."}


@app.post("/add")
async def add_text(text: str):
    global static_string
    static_string += text
    return {"message": "Text added", "Current_string": static_string}


@app.put("/change")
async def change_text(new_text: str):
    global static_string
    static_string = new_text
    return {"message": "Text changed", "Current_string": static_string}


@app.delete("/remove")
async def remove_text():
    global static_string
    static_string = ""
    return {"message": "Text removed"}
