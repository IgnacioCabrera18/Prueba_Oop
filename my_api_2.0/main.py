from fastapi import FastAPI, HTTPException
from typing import List
from model import UserCreateSchema, UserResponseSchema, UserUpdateSchema
from service import UserService
from persistence import UserRepository

repo = UserRepository()
service = UserService(repo)

app = FastAPI(title="API Usuarios 2.0", version="2.0")

@app.get("/", tags=["General"])
def home():
    return {"mensaje": "API Usuarios 2.0 funcionando"}

@app.get("/users", response_model=List[UserResponseSchema])
def get_all_users():
    users = service.get_users()
    if not users:
        raise HTTPException(status_code=404, detail="No se encontró usuarios")
    return users

@app.post("/users", response_model=UserResponseSchema)
def create_user(user: UserCreateSchema):
    return service.create_user(user)

@app.get("/users/{user_id}", response_model=UserResponseSchema)
def get_user_by_id(user_id):
    user = service.get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return user

@app.get("/users/search", response_model=UserResponseSchema)
def search_users(name: Optional[str] = None, min_age: Optional[int] = None, max_age: Optional[int] = None):
    return service.search_users(name=name, min_age=min_age, max_age=max_age)

@app.put("/users/{user_id}", response_model=UserResponseSchema)
def update_user(user_id: int, user_data: UserUpdateSchema):
    updated = service.update_user(user_id, user_data)
    if not updated:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return updated

@app.delete("/users/{user_id}", response_model=UserResponseSchema)
def delete_user(user_id: int):
    deleted = service.delete_user(user_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return {"mensaje": f"Usuario {user_id} eliminado con éxito"}
