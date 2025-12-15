from pydantic import BaseModel

class UserCreateSchema(BaseModel):
    name: str
    age: int
    rol: str

    class Config:
        from_attributes = True

class UserResponseSchema(BaseModel):
    id: int
    name: str
    age: int
    rol: str

    class Config:
        from_attributes = True
