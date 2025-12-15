from fastapi import FastAPI, HTTPException
from typing import List

from model import UserCreateSchema, UserResponseSchema
from service import UserService
from persistence import UserRepository

user_repository = UserRepository()


user_service = UserService(repository=user_repository)


app = FastAPI(
    title="API de Usuarios con Arquitectura en Capas",
    description="Un ejemplo de cómo estructurar una API en capas.",
    version="1.0.0"
)

@app.get("/", tags=["General"])
def home():
    return {"mensaje": "API de Usuarios funcionando"}

@app.get("/users", response_model=List[UserResponseSchema], tags=["Usuarios"])
def get_all_user():
    users = user_service.get_users()
    return users

@app.post("/users", response_model=UserResponseSchema, status_code=201, tags=["Usuarios"])
def create_users(user: UserCreateSchema):
    new_user = user_service.create_user(user_data=user)
    return new_user

@app.delete("/users/{user_id}", tags=["Usuarios"])
def delete_user(user_id: int):
    deleted = user_service.delete_users(user_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return {"mensaje": f"Usuario {user_id} eliminado con éxito"}
