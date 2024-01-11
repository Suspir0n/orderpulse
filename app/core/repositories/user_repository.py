from app.core.entities.user_entities import User
from app.core.adpters.mongo_adapter import MongoAdapter
from app.core.repositories.validations.validations_user import has_user_in_db, type_fields_valid, fields_required, has_user_id_valid

class UserRepository:
    def __init__(self):
        self.mongo_adapter = MongoAdapter()
        self.mongo_client = self.mongo_adapter.get_mongo_client()
        self.name_db = 'purchase_requests'
        self.name_collection = 'users'
        self.collection = self.mongo_adapter.get_collection(self.name_db, self.name_collection)

    def create_user(self, user_data) -> User:
        fields_required(user_data=user_data)
        type_fields_valid(user_data=user_data)

        is_existing_user = self.collection.find_one({'email': user_data['email']})
        has_user_in_db(is_existing_user=is_existing_user)

        return self.collection.insert_one(user_data)

    def get_user_by_id(self, user_id) -> User:
        has_user_id_valid(user_id)
        return self.collection.find_one({'_id': user_id})

    def get_all_users(self) -> User:
        result = self.collection.find()
        return list(result)

    def update_user(self, user_id, updated_data) -> User:
        has_user_id_valid(user_id)
        type_fields_valid(updated_data)

        return self.collection.update_one({'_id': user_id}, {'$set': updated_data})

    def delete_user(self, user_id) -> User:
        has_user_id_valid(user_id)
        return self.collection.delete_one({'_id': user_id})