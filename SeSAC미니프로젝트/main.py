from typing import Union
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def read_root():
    return {'Hello':'World'}

@app.get('/items/{item_id}')
async def read_item(item_id:int):
    return {'item_id':item_id}