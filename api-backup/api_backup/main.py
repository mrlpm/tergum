from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

vms = {'vm01': {'id': '123', 'ram': '5G'}, 'vm02': '456', 'vm03': '789'}

class Connection(BaseModel):
    url: str
    username: str
    password: str
    cert: str

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.post("/connection")
async def connection(conn: Connection):
    return {"Status": "200"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.get("/vms")
async def get_vm_list():
    return vms
