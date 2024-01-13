from app.core.repositories.user_repository import UserRepository

class GetByIdUserUseCase:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def execute(self, user_id: str):
        get_by_user = self.user_repository.get_user_by_id(user_id=user_id)

        return get_by_user