# models/usuario.py

from pydantic import BaseModel, Field, EmailStr
from typing import Optional

class UsuarioIn(BaseModel):
    nombre: str
    email: EmailStr
    telefono: str
    direccion: str

class UsuarioOut(UsuarioIn):
    id: str = Field(..., alias="_id")

class UsuarioUpdate(BaseModel):
    nombre: Optional[str] = None
    email: Optional[EmailStr] = None
    telefono: Optional[str] = None
    direccion: Optional[str] = None
