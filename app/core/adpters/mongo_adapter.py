from pymongo import MongoClient
import os
from dotenv import load_dotenv

class MongoAdapter:
    def __init__(self):
        load_dotenv()
        self.mongo_uri = os.getenv('MONGO_URI')
        self.mongo_username = os.getenv('MONGO_USERNAME')
        self.mongo_password = os.getenv('MONGO_PASSWORD')
        self.client = MongoClient(
            self.mongo_uri,
            username=self.mongo_username,
            password=self.mongo_password
        )

    def get_mongo_client(self):
        return self.client