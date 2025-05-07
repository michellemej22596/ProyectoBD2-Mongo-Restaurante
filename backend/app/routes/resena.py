# routes/resena.py
from fastapi import APIRouter, HTTPException
from app.models.resena import ResenaIn, ResenaOut, ResenaUpdate
from app.database import mongodb
from bson import ObjectId, errors
from typing import List

router = APIRouter()
resenas_collection = mongodb.get_db()["Reseñas"]

def resena_serializer(doc):
    doc["_id"] = str(doc["_id"])
    for platillo in doc.get("platillos", []):
        platillo.pop("platillo_id", None)
    return doc

@router.get("/count")
async def count_resenas():
    counts = await resenas_collection.aggregate([
        {"$group": {"_id": "$restaurante_nombre", "total_resenas": {"$sum": 1}}},
        {"$sort": {"total_resenas": -1}}
    ]).to_list(100)
    return counts

@router.get("/top")
async def top_restaurantes():
    ranking = await resenas_collection.aggregate([
        {"$group": {
            "_id": "$restaurante_nombre",
            "promedio_calificacion": {"$avg": "$calificacion"},
            "total_resenas": {"$sum": 1}
        }},
        {"$sort": {"promedio_calificacion": -1, "total_resenas": -1}},
        {"$limit": 10}
    ]).to_list(10)

    return ranking

@router.get("/", response_model=List[ResenaOut])
async def get_resenas():
    resenas = await resenas_collection.find().to_list(100)
    return [resena_serializer(r) for r in resenas]

@router.get("/{resena_id}", response_model=ResenaOut)
async def get_resena(resena_id: str):
    query = {}
    try:
        oid = ObjectId(resena_id)
        query = {"_id": oid}
    except errors.InvalidId:
        query = {"_id": int(resena_id)}

    resena = await resenas_collection.find_one(query)
    if not resena:
        raise HTTPException(status_code=404, detail="Reseña no encontrada")
    return resena_serializer(resena)

@router.post("/", response_model=ResenaOut)
async def create_resena(resena: ResenaIn):
    res = await resenas_collection.insert_one(resena.dict())
    new_resena = await resenas_collection.find_one({"_id": res.inserted_id})
    return resena_serializer(new_resena)

@router.put("/{resena_id}", response_model=ResenaOut)
async def update_resena(resena_id: str, resena: ResenaUpdate):
    query = {}
    try:
        oid = ObjectId(resena_id)
        query = {"_id": oid}
    except errors.InvalidId:
        query = {"_id": int(resena_id)}

    updated = await resenas_collection.find_one_and_update(
        query,
        {"$set": {k: v for k, v in resena.dict(exclude_none=True).items()}},
        return_document=True
    )
    if not updated:
        raise HTTPException(status_code=404, detail="Reseña no encontrada")

    return resena_serializer(updated)

@router.delete("/{resena_id}")
async def delete_resena(resena_id: str):
    query = {}
    try:
        oid = ObjectId(resena_id)
        query = {"_id": oid}
    except errors.InvalidId:
        query = {"_id": int(resena_id)}

    result = await resenas_collection.delete_one(query)
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Reseña no encontrada")
    return {"message": "Reseña eliminada correctamente"}
