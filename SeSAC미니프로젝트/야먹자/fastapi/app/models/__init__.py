# from motor.motor_asyncio import AsyncIOMotorClient
# from odmantic import AIOEngine
from app.config import MONGO_DB_NAME, MONGO_DB_URL
import pymongo

class MongoDB:
    
    def __init__(self):
        self.client = None
        self.db = None
        
    def connect(self):
        self.client = pymongo.MongoClient(MONGO_DB_URL, serverSelectionTimeoutMS=5000)
        self.db = self.client[MONGO_DB_NAME]
        # self.client = AsyncIOMotorClient(MONGO_DB_URL)
        # self.engine = AIOEngine(motor_client=self.client, database=MONGO_DB_NAME)
        print('DB와 성공적으로 연결이 되었습니다.')
        
    def close(self):
        self.client.close()
        print('DB와 연결이 끊어졌습니다.')
        
mongodb = MongoDB()
