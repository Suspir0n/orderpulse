from app.core.entities.user_entities import User
from app.core.repositories.user_repository import UserRepository

class CreateUserUseCase:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def execute(self, username: str, first_name: str, last_name: str, email: str, password: str) -> User:
        new_user = User(username=username, first_name=first_name, last_name=last_name, email=email, password=password)
        created_user = self.user_repository.create_user(new_user.to_dict())

        return created_user