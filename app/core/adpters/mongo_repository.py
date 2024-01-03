from pymongo import MongoClient
from bson.objectid import ObjectId

class MongoDBRepository:
    def __init__(self, connection_string, database_name, collection_name):
        self.client = MongoClient(connection_string)
        self.db = self.client[database_name]
        self.collection = self.db[collection_name]

    def create(self, data):
        result = self.collection.insert_one(data)
        return str(result.inserted_id)

    def read(self, query):
        return self.collection.find_one(query)

    def update(self, query, data):
        result = self.collection.update_one(query, {"$set": data})
        return result.modified_count > 0

    def delete(self, query):
        result = self.collection.delete_one(query)
        return result.deleted_count > 0

    def read_all(self, query=None):
        if query is None:
            return list(self.collection.find())
        return list(self.collection.find(query))

    def delete_all(self, query=None):
        if query is None:
            result = self.collection.delete_many({})
        else:
            result = self.collection.delete_many(query)
        return result.deleted_count
