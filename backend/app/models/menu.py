# models/menu.py

from pydantic import BaseModel, Field
from typing import Optional

class PlatilloIn(BaseModel):
    nombre: str
    descripcion: str
    precio: float
    restaurante_id: str

class PlatilloOut(PlatilloIn):
    id: str = Field(..., alias="_id")

class PlatilloUpdate(BaseModel):
    nombre: Optional[str] = None
    descripcion: Optional[str] = None
    precio: Optional[float] = None
    restaurante_id: Optional[str] = None
