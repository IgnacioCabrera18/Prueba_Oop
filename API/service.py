from typing import List
from model imprt UserCreateSchema, UserResponseShema
from persistence import UserRepository


class UserService:
    def __init__(self, repository):
        self.repository = repository

    def create_user(self, user_data: UserCreateSchema) -> UserRepository:
        new_id = self.repository.add(
            name=user_data.name,
            age=user_data.age,
            rol=user_data.rol
        )
        new_user = self.repository.get_by_id(new_id)
        return UserResponseShema(**new_user)

    def get_users(self) -> List[UserResponseShema]:
        user_dict = self.repository.get_all
        return [UserResponseShema(**user) for user in user_dict]

    def delete_user(self, user_id: int) -> bool:
        return self.repository.delete(user_id=user_id)
