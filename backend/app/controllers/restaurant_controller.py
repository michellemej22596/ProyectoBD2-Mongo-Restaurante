# app/controllers/restaurant_controller.py
from fastapi import APIRouter, HTTPException, status
from app.models.restaurant import RestaurantCreate, RestaurantResponse
from app.config import database
from bson import ObjectId

router = APIRouter(prefix="/restaurantes", tags=["restaurantes"])

@router.get("/", response_model=list[RestaurantResponse])
async def get_restaurantes():
    restaurantes = await database["Restaurantes"].find().to_list(100)
    return [RestaurantResponse(**rest) for rest in restaurantes]

@router.get("/{restaurante_id}", response_model=RestaurantResponse)
async def get_restaurante(restaurante_id: str):
    try:
        restaurante = await database["Restaurantes"].find_one({"_id": ObjectId(restaurante_id)})
        if not restaurante:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Restaurante no encontrado"
            )
        return RestaurantResponse(**restaurante)
    except:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="ID inválido"
        )

@router.post("/", response_model=RestaurantResponse, status_code=status.HTTP_201_CREATED)
async def create_restaurante(restaurant: RestaurantCreate):
    restaurant_dict = restaurant.dict()
    result = await database["Restaurantes"].insert_one(restaurant_dict)
    new_restaurante = await database["Restaurantes"].find_one({"_id": result.inserted_id})
    return RestaurantResponse(**new_restaurante)

@router.put("/{restaurante_id}", response_model=RestaurantResponse)
async def update_restaurante(restaurante_id: str, restaurant: RestaurantCreate):
    try:
        restaurant_dict = restaurant.dict()
        result = await database["Restaurantes"].update_one(
            {"_id": ObjectId(restaurante_id)},
            {"$set": restaurant_dict}
        )
        if result.matched_count == 0:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Restaurante no encontrado"
            )
        updated_restaurante = await database["Restaurantes"].find_one({"_id": ObjectId(restaurante_id)})
        return RestaurantResponse(**updated_restaurante)
    except:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="ID inválido"
        )

@router.delete("/{restaurante_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_restaurante(restaurante_id: str):
    try:
        result = await database["Restaurantes"].delete_one({"_id": ObjectId(restaurante_id)})
        if result.deleted_count == 0:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Restaurante no encontrado"
            )
    except:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="ID inválido"
        )
