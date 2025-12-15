from typing import List, Optional
from model import UserCreateSchema, UserResponseSchema, UserUpdateSchema
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

    def search_users(self, name: str = "", min_age: int = None, max_age: int = None) -> List[UserResponseSchema]:
        users = self.repository.search(name, min_age, max_age)
        return [UserResponseSchema(**u) for u in users]

    def update_user(self, user_id: int, user_data: UserUpdateSchema) -> Optional[UserResponseSchema]:
        updated = self.repository.update(
            user_id,
            user_data.name,
            user_data.age,
            user_data.rol
        )
        if not updated:
            return None
        user = self.repository.get_by_id(user_id)
        return UserResponseSchema(**user)

    def delete_user(self, user_id: int) -> bool:
        return self.repository.delete(user_id)
