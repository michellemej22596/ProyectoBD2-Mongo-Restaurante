from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime

class OrdenItem(BaseModel):
    platillo_id: str
    cantidad: int
    precio: float

class OrdenIn(BaseModel):
    usuario_id: str
    items: List[OrdenItem]
    total: float
    estado: str
    fecha: datetime

class OrdenOut(OrdenIn):
    id: str = Field(..., alias="_id")

class OrdenUpdate(BaseModel):
    items: Optional[List[OrdenItem]] = None
    total: Optional[float] = None
    estado: Optional[str] = None
