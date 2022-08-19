from fastapi import FastAPI
from fastapi.responses import FileResponse
<<<<<<< HEAD
from typing import Union
from pydantic import BaseModel
=======
>>>>>>> a3882771f7a66de54026d77f631c547d26b3ce5d
import uvicorn

app = FastAPI()

# @app.get('/')
# def 작명():
#     return 'Hello'

# 파이썬 파일을 실행해도 uvicorn이 자동실행 되도록 하는 명령어
if __name__ == '__main__':
    uvicorn.run(app, host = '127.0.0.1', port = 8000, debug=True)

# class Item(BaseModel):
#     name : str
#     price : float
#     is_offer : Union[bool, None] = None

@app.get('/')
def root():
    return {'Hello':'World'}

# @app.get('/items/{item_id}')
# def read_item(item_id:int, q:Union[str, None]=None):
#     return {'item_id':item_id, 'q':q}

# @app.put('/items/{item_id}')
# def update_item(item_id:int, item:Item):
#     return {'item_name':item.name, 'item_id':item_id, 'item_price':item.price}

<<<<<<< HEAD
@app.get('/fileresponse')
=======
@app.get('/data')
>>>>>>> a3882771f7a66de54026d77f631c547d26b3ce5d
def data():
    return FileResponse('folium_test.html')