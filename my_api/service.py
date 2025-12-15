from typing import List
from model import UserCreateSchema, UserResponseSchema
from persistence import UserRepository

class UserService:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    def create_user(self, user_data: UserCreateSchema) -> UserResponseSchema:
        new_id = self.repository.add(user_data.name, user_data.age, user_data.rol)
        new_user = self.repository.get_by_id(new_id)
        return UserResponseSchema(**new_user)

    def get_users(self) -> List[UserResponseSchema]:
        users = self.repository.get_all()
        return [UserResponseSchema(**u) for u in users]
    
    def get_user(self, user_id):
        user = self.repository.get_by_id(user_id)
        if not user:
            return None
        return UserResponseSchema(**user)

    def search_users_by_name(self, name: str) -> List[UserResponseSchema]:
        users = self.repository.get_by_name(name)
        return [UserResponseSchema(**u) for u in users]

    def delete_user(self, user_id: int) -> bool:
        return self.repository.delete(user_id)
