# app/models/user.py
from pydantic import BaseModel, EmailStr
from bson import ObjectId
from typing import Optional

# Modelo para la validación de datos (Pydantic)
class UserBase(BaseModel):
    nombre: str
    email: EmailStr
    telefono: str
    direccion: str

# Para interactuar con MongoDB, vamos a usar ObjectId
class UserInDB(UserBase):
    id: ObjectId

    class Config:
        orm_mode = True

# Modelo para recibir datos al crear un usuario
class UserCreate(UserBase):
    pass

# Modelo para responder con datos de usuario
class UserResponse(UserBase):
    id: str
