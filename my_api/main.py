from fastapi import FastAPI, HTTPException
from typing import List
from model import UserCreateSchema, UserResponseSchema
from service import UserService
from persistence import UserRepository

user_repository = UserRepository()
user_service = UserService(repository=user_repository)

app = FastAPI(
    title="API de Usuarios - Ejercicio Guiado",
    description="API práctica para aprender arquitectura en capas",
    version="1.0.0"
)

@app.get("/", tags=["General"])
def home():
    return {"mensaje": "API de Usuarios funcionando"}

@app.get("/users", response_model=List[UserResponseSchema], tags=["Usuarios"])
def get_all_users():
    users = user_service.get_users()
    return users

@app.post("/users", response_model=UserResponseSchema, status_code=201)
def create_user(user: UserCreateSchema):
    new_user = user_service.create_user(user)
    return new_user

@app.get("/users/{user_id}")
def get_user_by_id(user_id: int):
    user = user_service.get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return user

@app.get("/users/search")
def get_users_by_name(name: str):
    users = user_service.search_users_by_name(name)
    return users

@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    deleted = user_service.delete_user(user_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return {"mensaje": f"Usuario {user_id} eliminado con éxito"}
