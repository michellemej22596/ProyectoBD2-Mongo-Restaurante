# app/models/restaurant.py
from pydantic import BaseModel
from bson import ObjectId
from typing import Optional, List

# Modelo para la validación de datos (Pydantic)
class RestaurantBase(BaseModel):
    nombre: str
    direccion: str
    telefono: str
    categoria: str
    # Si el menú y las reseñas son listas vacías, los dejamos como List[dict] para permitir su inclusión
    menu: Optional[List[dict]] = []
    reseñas: Optional[List[dict]] = []

# Para interactuar con MongoDB, usamos ObjectId
class RestaurantInDB(RestaurantBase):
    id: ObjectId

    class Config:
        orm_mode = True

# Modelo para recibir datos al crear un restaurante
class RestaurantCreate(RestaurantBase):
    pass

# Modelo para responder con datos del restaurante
class RestaurantResponse(RestaurantBase):
    id: str
