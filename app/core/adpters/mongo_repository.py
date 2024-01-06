class MongoRepository:
    def __init__(self, mongo_client):
        self.mongo_client = mongo_client

    def create_user(self, user_data):
        self.mongo_client.users.insert_one(user_data)

    def get_user_by_id(self, user_id):
        return self.mongo_client.users.find_one({'uuid': user_id})

    def get_all_user(self):
        return self.mongo_client.users.find()

    def get_update_user(self, old_data, new_data):
        return self.mongo_client.users.replace_one(old_data, new_data, True)

