from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime

class Item(BaseModel):
    nombre: str
    descripcion: str
    precio: float
    cantidad: int
    platillo_id: Optional[str] = None  # opcional

class OrdenIn(BaseModel):
    usuario_id: str
    items: List[Item]
    total: float
    estado: str
    fecha: datetime

class OrdenOut(OrdenIn):
    id: str = Field(..., alias="_id")

class OrdenUpdate(BaseModel):
    items: Optional[List[Item]]
    total: Optional[float]
    estado: Optional[str]
