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

    def close_connection(self):
        self.client.close()

    def get_database(self, database_name):
        return self.client[database_name]

    def get_collection(self, database_name, collection_name):
        db = self.get_database(database_name)
        return db[collection_name]

    def check_connection(self):
        try:
            self.client.admin.command('ismaster')
            return True
        except Exception as e:
            raise ConnectionError("Failed to establish a connection.")