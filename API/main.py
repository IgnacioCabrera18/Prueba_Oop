from fastapi import FastAPI
from typing import List
from model import UserCreateSchema, UserResponseShema
from service import UserService
from persistence import UserRepository

user_repository = UserRepository()
user_service = UserService(repository=user_repository)

app = FastAPI()

@app.get("/")
def home():
    return {"mensaje": "Hola buenas tardes"}


@app.get("/users", response_model=List[UserResponseShema])
def get_all_users():
    users = user_service.get_users()
    return user

@app.post("/users", response_model=UserResponseShema)
def create_user(user):
    new_user = user_service.create_user(user_data=user)
    return new_user
    

@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    delete = user_service.delete_users(user_id=user_id)
