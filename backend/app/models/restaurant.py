from typing import List, Optional, Union
from pydantic import BaseModel, Field, validator
from bson import ObjectId

class RestaurantBase(BaseModel):
    nombre: str
    direccion: str
    telefono: str
    categoria: str
    menu: List[str] = Field(default_factory=list)
    resenas: List[str] = Field(default_factory=list)
    location: List[float] = Field(..., min_items=2, max_items=2)

class RestaurantCreate(RestaurantBase):
    pass

class RestaurantResponse(RestaurantBase):
    id: Union[int, str] = Field(alias="_id")  # Accepts both numeric and string IDs

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}

    @validator('id', pre=True)
    def validate_id(cls, v):
        # Convert ObjectId to string if it's an ObjectId
        if isinstance(v, ObjectId):
            return str(v)
        # Otherwise keep as is (could be int or str)
        return v