
# Item model should be defined separately (app/models/item.py)
class Item(BaseModel):
    # Define your item fields based on what's in the array objects
    item_id: Union[int, str]
    nombre: str
    precio: float
    cantidad: int

class OrdenBase(BaseModel):
    usuario_id: Union[int, str]
    items: List[Item]
    total: float
    estado: str = Field(..., regex="^(pendiente|completado|cancelado)$")
    fecha: datetime

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}

class OrdenCreate(OrdenBase):
    pass

class OrdenResponse(OrdenBase):
    id: Union[int, str, PyObjectId] = Field(alias="_id")

    class Config:
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "_id": 1,
                "usuario_id": 1,
                "items": [
                    {"item_id": 1, "nombre": "Hamburguesa", "precio": 120, "cantidad": 1},
                    {"item_id": 2, "nombre": "Refresco", "precio": 25, "cantidad": 2}
                ],
                "total": 245,
                "estado": "pendiente",
                "fecha": "2025-04-30T05:36:07.520+00:00"
            }
        }