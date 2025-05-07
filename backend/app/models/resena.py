# models/resena.py

from pydantic import BaseModel, Field
from typing import List, Optional

class PlatilloResena(BaseModel):
    platillo_id: str
    nombre: str

class ResenaIn(BaseModel):
    usuario_nombre: str
    restaurante_nombre: str
    platillos: List[PlatilloResena]
    calificacion: int
    comentario: str

class ResenaOut(ResenaIn):
    id: str = Field(..., alias="_id")

class ResenaUpdate(BaseModel):
    platillos: Optional[List[PlatilloResena]] = None
    calificacion: Optional[int] = None
    comentario: Optional[str] = None
