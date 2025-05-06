# routes/restaurante.py

from fastapi import APIRouter, HTTPException
from app.models.restaurante import RestauranteIn, RestauranteOut, RestauranteUpdate
from app.database import mongodb
from bson import ObjectId
from typing import List

router = APIRouter()

# Usar la colección correcta (Restaurantes con R mayúscula)
restaurantes_collection = mongodb.get_db()["Restaurantes"]

def restaurante_serializer(doc):
    doc["_id"] = str(doc["_id"])
    return doc

@router.get("/", response_model=List[RestauranteOut])
async def get_restaurantes():
    restaurantes = await restaurantes_collection.find().to_list(100)
    return [restaurante_serializer(r) for r in restaurantes]

@router.get("/{restaurante_id}", response_model=RestauranteOut)
async def get_restaurante(restaurante_id: str):
    restaurante = await restaurantes_collection.find_one({"_id": ObjectId(restaurante_id)})
    if not restaurante:
        raise HTTPException(status_code=404, detail="Restaurante no encontrado")
    return restaurante_serializer(restaurante)

@router.post("/", response_model=RestauranteOut)
async def create_restaurante(restaurante: RestauranteIn):
    res = await restaurantes_collection.insert_one(restaurante.dict())
    new_restaurante = await restaurantes_collection.find_one({"_id": res.inserted_id})
    return restaurante_serializer(new_restaurante)

@router.put("/{restaurante_id}", response_model=RestauranteOut)
async def update_restaurante(restaurante_id: str, restaurante: RestauranteUpdate):
    updated = await restaurantes_collection.find_one_and_update(
        {"_id": ObjectId(restaurante_id)},
        {"$set": {k: v for k, v in restaurante.dict(exclude_none=True).items()}},
        return_document=True
    )
    if not updated:
        raise HTTPException(status_code=404, detail="Restaurante no encontrado")
    return restaurante_serializer(updated)

@router.delete("/{restaurante_id}")
async def delete_restaurante(restaurante_id: str):
    result = await restaurantes_collection.delete_one({"_id": ObjectId(restaurante_id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Restaurante no encontrado")
    return {"message": "Restaurante eliminado correctamente"}

@router.get("/cercanos/ubicacion", response_model=List[RestauranteOut])
async def get_restaurantes_cercanos(lat: float, lng: float):
    cursor = restaurantes_collection.aggregate([
        {
            "$geoNear": {
                "near": {"type": "Point", "coordinates": [lng, lat]},
                "distanceField": "distancia",
                "spherical": True,
                "limit": 5
            }
        }
    ])
    restaurantes = []
    async for doc in cursor:
        restaurantes.append(restaurante_serializer(doc))
    return restaurantes
