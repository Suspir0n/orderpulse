class MongoRepository:
    def __init__(self, mongo_client):
        self.mongo_client = mongo_client

    def create_user_one(self, user_data):
        return self.mongo_client.users.insert_one(user_data)

    def create_user_many(self, users_data):
        return self.mongo_client.users.insert_many(users_data)

    def get_user_by_id(self, _id):
        return self.mongo_client.users.find_one({'_id': _id})

    def get_all_user(self):
        return self.mongo_client.users.find()

    def get_update_user(self, _id, new_data):
        return self.mongo_client.users.replace_one({'_id': _id}, new_data)

