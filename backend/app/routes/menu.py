# routes/menu.py

from fastapi import APIRouter, HTTPException, Query
from app.models.menu import PlatilloIn, PlatilloOut, PlatilloUpdate
from app.database import mongodb
from bson import ObjectId, errors
from typing import List

router = APIRouter()

menu_collection = mongodb.get_db()["Menu"]

def platillo_serializer(doc):
    doc["_id"] = str(doc["_id"])
    return doc

@router.get("/", response_model=List[PlatilloOut])
async def get_platillos(skip: int = 0, limit: int = 10, precio_min: float = 0, precio_max: float = 10000):
    platillos = await menu_collection.find({
        "precio": {"$gte": precio_min, "$lte": precio_max}
    }).skip(skip).limit(limit).to_list(limit)

    return [platillo_serializer(p) for p in platillos]

@router.get("/{platillo_id}", response_model=PlatilloOut)
async def get_platillo(platillo_id: str):
    try:
        oid = ObjectId(platillo_id)
        query = {"_id": oid}
    except errors.InvalidId:
        query = {"_id": int(platillo_id)}

    platillo = await menu_collection.find_one(query)
    if not platillo:
        raise HTTPException(status_code=404, detail="Platillo no encontrado")

    return platillo_serializer(platillo)

@router.post("/", response_model=PlatilloOut)
async def create_platillo(platillo: PlatilloIn):
    res = await menu_collection.insert_one(platillo.dict())
    new_platillo = await menu_collection.find_one({"_id": res.inserted_id})
    return platillo_serializer(new_platillo)

@router.put("/{platillo_id}", response_model=PlatilloOut)
async def update_platillo(platillo_id: str, platillo: PlatilloUpdate):
    try:
        oid = ObjectId(platillo_id)
        query = {"_id": oid}
    except errors.InvalidId:
        query = {"_id": int(platillo_id)}

    updated = await menu_collection.find_one_and_update(
        query,
        {"$set": {k: v for k, v in platillo.dict(exclude_none=True).items()}},
        return_document=True
    )
    if not updated:
        raise HTTPException(status_code=404, detail="Platillo no encontrado")

    return platillo_serializer(updated)

@router.delete("/{platillo_id}")
async def delete_platillo(platillo_id: str):
    try:
        oid = ObjectId(platillo_id)
        query = {"_id": oid}
    except errors.InvalidId:
        query = {"_id": int(platillo_id)}

    result = await menu_collection.delete_one(query)
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Platillo no encontrado")
    return {"message": "Platillo eliminado correctamente"}

# BULK INSERT
@router.post("/bulk")
async def bulk_create_platillos(platillos: List[PlatilloIn]):
    docs = [p.dict() for p in platillos]
    result = await menu_collection.insert_many(docs)
    new_platillos = await menu_collection.find({"_id": {"$in": result.inserted_ids}}).to_list(len(result.inserted_ids))
    return [platillo_serializer(p) for p in new_platillos]

# BULK UPDATE precios (incrementar porcentaje)
@router.patch("/actualizar-precios")
async def bulk_update_prices(incremento: float):
    result = await menu_collection.update_many({}, {"$mul": {"precio": 1 + incremento}})
    return {"message": f"{result.modified_count} platillos actualizados."}

# BULK DELETE por restaurante_id
@router.delete("/eliminar-por-restaurante/{restaurante_id}")
async def bulk_delete_por_restaurante(restaurante_id: str):
    result = await menu_collection.delete_many({"restaurante_id": restaurante_id})
    return {"message": f"{result.deleted_count} platillos eliminados."}
