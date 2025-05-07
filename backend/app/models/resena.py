# models/resena.py
from typing import List, Optional
from pydantic import BaseModel

class Platillo(BaseModel):
    nombre: str
    descripcion: str
    precio: Optional[float] = None  # Opcional

class ResenaIn(BaseModel):
    usuario_nombre: str
    restaurante_nombre: str
    platillos: List[Platillo]
    calificacion: int
    comentario: str

class ResenaUpdate(BaseModel):
    platillos: Optional[List[Platillo]] = None
    calificacion: Optional[int] = None
    comentario: Optional[str] = None

class ResenaOut(BaseModel):
    usuario_nombre: str
    restaurante_nombre: str
    platillos: List[Platillo]
    calificacion: int
    comentario: str