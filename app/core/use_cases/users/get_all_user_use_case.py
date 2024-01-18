from app.core.repositories.user_repository import UserRepository

class GetAllUserUseCase:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def execute(self):
        get_all_users = self.user_repository.get_all_users()

        return get_all_users