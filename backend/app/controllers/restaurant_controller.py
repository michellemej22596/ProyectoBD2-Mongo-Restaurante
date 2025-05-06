from fastapi import APIRouter, HTTPException
from app.models.restaurant import RestaurantCreate, RestaurantResponse
from typing import List, Optional, Union
from app.config import database

router = APIRouter(prefix="/api/restaurantes", tags=["restaurantes"])

@router.get("/", response_model=List[RestaurantResponse])
async def get_restaurantes():
    restaurantes = await database["Restaurantes"].find().to_list(None)

    # Convert each restaurant document to a dictionary and handle _id
    restaurant_list = []
    for rest in restaurantes:
        rest_dict = dict(rest)
        rest_dict["_id"] = rest_dict["_id"]  # Keep as is (int or ObjectId)
        restaurant_list.append(rest_dict)

    return [RestaurantResponse(**rest) for rest in restaurant_list]