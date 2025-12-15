from typing import List
from persistence import UserRepository
from model import UserCreateSchema, UserResponseSchema

class UserService:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    def create_user(self, user_data: UserCreateSchema) -> UserResponseSchema:
        new_id = self.repository.add(
            name=user_data.name,
            age=user_data.age,
            rol=user_data.rol
        )
        
        new_user = self.repository.get_by_id(new_id)
        return UserResponseSchema(**new_user)

    def get_users(self) -> List[UserResponseSchema]:
        user_to_dict = self.repository.get_all()
        return [UserResponseSchema(**user) for user in user_to_dict]

    def delete_users(self, user_id: int) -> bool:
        return self.repository.delete(user_id)
