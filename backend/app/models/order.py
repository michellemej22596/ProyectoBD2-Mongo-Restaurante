from datetime import datetime
from typing import List, Optional, Union
from pydantic import BaseModel, Field
from bson import ObjectId
from app.models.item import Item  # You'll need to create this Item model

# Helper for handling both numeric and ObjectId IDs
class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if isinstance(v, int):
            return str(v)  # Convert numeric IDs to string
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid ObjectId")
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")
