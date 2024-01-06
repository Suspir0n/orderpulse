from bson.objectid import ObjectId

class MongoRepository:
    def __init__(self, mongo_client):
        self.mongo_client = mongo_client

    def create_user_one(self, user_data):
        all_fields = ['username', 'first_name', 'last_name', 'email', 'password']
        required_fields = ['username', 'email', 'password']

        for field in required_fields:
            if field not in user_data:
                raise ValueError(f"The required field '{field}' is missing from the user data.")

        for field in all_fields:
            if not isinstance(user_data[field], str):
                raise TypeError("All fields must be strings.")

        is_existing_user = self.mongo_client.users.find_one({'email': user_data['email']})
        if is_existing_user:
            raise ValueError("There is already a user with this email.")

        return self.mongo_client.users.insert_one(user_data)

    def create_user_many(self, users_data):

        return self.mongo_client.users.insert_many(users_data)

    def get_user_by_id(self, _id):
        if not ObjectId.is_valid(_id):
            raise ValueError("Invalid user ID.")

        return self.mongo_client.users.find_one({'_id': _id})

    def get_all_user(self):
        return self.mongo_client.users.find()

    def get_update_user(self, _id, new_data):
        return self.mongo_client.users.replace_one({'_id': _id}, new_data)

