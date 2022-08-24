from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse 
from fastapi.templating import Jinja2Templates # 템플릿 엔진
from app.config import BASE_DIR # 현재 config.py가 있는 주소를 반환
from app.models import mongodb
from app.models.hate_menu import Hate
from app.models.map_maker import Make_map

app = FastAPI()
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))

'''
1. 메인 페이지
2. 입력 값을 받아 DB에서 서치 후 좌표 및 기타 정보 리턴
3. 리턴 된 정보로 folium 맵 리턴
4. 리턴 받은 html 파일을 web에 출력
'''

@app.get("/",  response_class=HTMLResponse)
def read_item(request: Request):
    context = {"request":request}
    return templates.TemplateResponse("index.html", context)

@app.get("/input", response_class=HTMLResponse)
async def input(request : Request):
    # 1. 쿼리에서 제외할 음식 추출
    keyword = request.query_params.get("q")  # 쿼리에서 키워드 추출
    # (예외처리)
    # 1) 입력받은 값이 없는 경우
    if not keyword:  # 키워드가 없다면 사용자에게 검색을 요구
        context = {"request": request}
        return templates.TemplateResponse("index.html", context=context)
    else :
        map_info = mongodb.db['ya'].find()
        df = Make_map.load_data(map_info)
        map_info= Make_map.makemap(df)
        context = {"request":request, 'map':map_info}
        return templates.TemplateResponse('index.html', context)

# app이 시작될 때 실행
@app.on_event('startup')
def on_app_start():
    mongodb.connect()


# app이 멈출 때 실행
@app.on_event('shutdown')
def on_app_shutdown():
    mongodb.close()