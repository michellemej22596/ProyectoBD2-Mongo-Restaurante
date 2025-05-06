from pydantic import BaseModel, EmailStr, Field, validator
from bson import ObjectId
from typing import Optional
from pydantic.json import ENCODERS_BY_TYPE

# Add ObjectId to Pydantic's JSON encoders
ENCODERS_BY_TYPE[ObjectId] = str

class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid ObjectId")
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")

class UserBase(BaseModel):
    nombre: str = Field(..., min_length=1, max_length=50)
    email: EmailStr
    telefono: str = Field(..., min_length=8, max_length=15)
    direccion: str = Field(..., min_length=5, max_length=100)

class UserInDB(UserBase):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")

    class Config:
        allow_population_by_field_name = True
        json_encoders = {ObjectId: str}
        arbitrary_types_allowed = True

class UserCreate(UserBase):
    pass

class UserResponse(UserBase):
    id: str = Field(..., alias="_id")

    class Config:
        allow_population_by_field_name = True