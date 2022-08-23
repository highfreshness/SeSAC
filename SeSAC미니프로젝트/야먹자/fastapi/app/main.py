from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app.config import BASE_DIR # 현재 config.py가 있는 주소를 반환

app = FastAPI()
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))

'''
1. 메인 페이지vci
2. 입력 값을 받아 DB에서 서치 후 좌표 및 기타 정보 리턴
3. 리턴 된 정보로 folium 맵 리턴
4. 리턴 받은 html 파일을 web에 출력
'''

@app.get("/",  response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse("index.html", {"request":request})