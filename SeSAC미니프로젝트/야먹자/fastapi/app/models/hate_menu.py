from odmantic import Model

class Hate(Model):
    stores: str
    category: str
    X: str
    Y: str
    road_address: str
    place_url: str
    menu: str
    category: str
    business_hours: str
    rating: str
    phone_number: str
    last_update: str
    
    
    class Config: # 대소문자 다르면 파이썬 파일 이름으로 저정됨
        collection = "ya" # DB -> collection(=table) -> document