# models/restaurante.py

from pydantic import BaseModel, Field
from typing import List, Optional
from bson import ObjectId

class Platillo(BaseModel):
    platillo_id: Optional[str]
    nombre: str
    precio: float

class Reseña(BaseModel):
    usuario_id: Optional[str]
    calificacion: int
    comentario: str

class RestauranteIn(BaseModel):
    nombre: str
    direccion: str
    telefono: str
    categoria: str
    menu: List[Platillo] = []
    reseñas: List[Reseña] = []
    location: List[float] = Field(..., description="Lista con [latitud, longitud]")

class RestauranteOut(RestauranteIn):
    id: str = Field(..., alias="_id")

class RestauranteUpdate(BaseModel):
    nombre: Optional[str]
    direccion: Optional[str]
    telefono: Optional[str]
    categoria: Optional[str]
    menu: Optional[List[Platillo]]
    reseñas: Optional[List[Reseña]]
    location: Optional[List[float]]
