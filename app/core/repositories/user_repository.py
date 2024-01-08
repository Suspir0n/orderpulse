from app.core.entities.user_entities import User
from app.core.adpters.mongo_adapter import MongoAdapter
from app.core.repositories.validations.validations_user import has_user_in_db, type_fields_valid, fields_required, has_user_id_valid

class UserRepository:
    def __init__(self):
        self.mongo_adapter = MongoAdapter()
        self.mongo_client = self.mongo_adapter.get_mongo_client()
        self.collections = self.mongo_client.users

    def create_user(self, user_data) -> User:
        fields_required(user_data=user_data)
        type_fields_valid(user_data=user_data)

        is_existing_user = self.mongo_client.users.find_one({'email': user_data['email']})
        has_user_in_db(is_existing_user=is_existing_user)

        return self.collections.insert_one(user_data)

    def get_user_by_id(self, user_id) -> User:
        has_user_id_valid(user_id)
        return self.collections.find_one({'_id': user_id})

    def get_all_users(self) -> User:
        return self.collections.find()

    def update_user(self, user_id, new_data) -> User:
        has_user_id_valid(user_id)
        type_fields_valid(new_data)

        is_existing_user = self.mongo_client.users.find_one({'_id': user_id})
        has_user_in_db(is_existing_user)
        return self.collections.update_one({'_id': user_id}, new_data)

    def delete_user(self, user_id) -> User:
        has_user_id_valid(user_id)
        return self.collections.delete_one({'_id': user_id})