# app/models/restaurant.py
from pydantic import BaseModel, validator
from bson import ObjectId
from typing import Optional

# Modelo base para un restaurante
class RestaurantBase(BaseModel):
    nombre: str
    direccion: str
    telefono: str
    categoria: str
    menu: Optional[list] = []
    reseñas: Optional[list] = []

    # Validar el id solo cuando sea necesario
    @validator('id', pre=True, always=True)
    def validate_id(cls, v):
        # Si es un ObjectId, convertirlo a string
        if isinstance(v, ObjectId):
            return str(v)
        return v

    class Config:
        arbitrary_types_allowed = True  # Permitir tipos arbitrarios como ObjectId

# Modelo para interactuar con MongoDB
class RestaurantInDB(RestaurantBase):
    id: ObjectId

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True  # Permitir tipos arbitrarios como ObjectId

# Para crear un restaurante
class RestaurantCreate(RestaurantBase):
    pass

# Para responder con los detalles de un restaurante
class RestaurantResponse(RestaurantBase):
    id: str  # Ahora el id será un string, ya que lo convertimos al validarlo
