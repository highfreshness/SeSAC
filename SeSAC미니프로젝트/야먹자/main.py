from fastapi import FastAPI
from fastapi.responses import FileResponse
from typing import Union
from pydantic import BaseModel
import uvicorn

app = FastAPI()

# @app.get('/')
# def 작명():
#     return 'Hello'

# 파이썬 파일을 실행해도 uvicorn이 자동실행 되도록 하는 명령어
if __name__ == '__main__':
    uvicorn.run(app, host = '0.0.0.0', port = 8000)

class Item(BaseModel):
    name : str
    price : float
    is_offer : Union[bool, None] = None

@app.get('/')
def read_root():
    return {'Hello':'World'}

# @app.get('/items/{item_id}')
# def read_item(item_id:int, q:Union[str, None]=None):
#     return {'item_id':item_id, 'q':q}

# @app.put('/items/{item_id}')
# def update_item(item_id:int, item:Item):
#     return {'item_name':item.name, 'item_id':item_id, 'item_price':item.price}

@app.get('/fileresponse')
def data():
    return FileResponse('folium_test.html')