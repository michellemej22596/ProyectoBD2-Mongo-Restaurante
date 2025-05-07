from fastapi import APIRouter, HTTPException
from app.models.orden import OrdenIn, OrdenOut, OrdenUpdate
from app.database import mongodb
from bson import ObjectId, errors
from typing import List

router = APIRouter()

ordenes_collection = mongodb.get_db()["Ordenes"]

def orden_serializer(doc):
    doc["_id"] = str(doc["_id"])

    items = []
    for item in doc.get("items", []):
        items.append({
            "nombre": item.get("nombre", ""),
            "descripcion": item.get("descripcion", ""),
            "precio": item.get("precio", 0),
            "cantidad": item.get("cantidad", 0)
        })

    doc["items"] = items
    return doc


@router.get("/", response_model=List[OrdenOut])
async def get_ordenes(skip: int = 0, limit: int = 10):
    ordenes = await ordenes_collection.find().sort("fecha", -1).skip(skip).limit(limit).to_list(limit)
    return ordenes

@router.get("/{orden_id}", response_model=OrdenOut)
async def get_orden(orden_id: str):
    query = {}
    try:
        oid = ObjectId(orden_id)
        query = {"_id": oid}
    except errors.InvalidId:
        query = {"_id": int(orden_id)}

    orden = await ordenes_collection.find_one(query)
    if not orden:
        raise HTTPException(status_code=404, detail="Orden no encontrada")

    return orden_serializer(orden)

@router.get("/usuario/{usuario_id}", response_model=List[OrdenOut])
async def get_ordenes_usuario(usuario_id: str):
    query = {}
    try:
        oid = ObjectId(usuario_id)
        query = {"usuario_id": oid}
    except errors.InvalidId:
        query = {"usuario_id": int(usuario_id)}

    ordenes = await ordenes_collection.find(query).to_list(100)
    return [orden_serializer(o) for o in ordenes]

@router.post("/", response_model=OrdenOut)
async def create_orden(orden: OrdenIn):
    res = await ordenes_collection.insert_one(orden.dict())
    new_orden = await ordenes_collection.find_one({"_id": res.inserted_id})
    return orden_serializer(new_orden)

@router.put("/{orden_id}", response_model=OrdenOut)
async def update_orden(orden_id: str, orden: OrdenUpdate):
    query = {}
    try:
        oid = ObjectId(orden_id)
        query = {"_id": oid}
    except errors.InvalidId:
        query = {"_id": int(orden_id)}

    updated = await ordenes_collection.find_one_and_update(
        query,
        {"$set": {k: v for k, v in orden.dict(exclude_none=True).items()}},
        return_document=True
    )
    if not updated:
        raise HTTPException(status_code=404, detail="Orden no encontrada")

    return orden_serializer(updated)

@router.patch("/{orden_id}/estado")
async def cambiar_estado_orden(orden_id: str, estado: str):
    query = {}
    try:
        oid = ObjectId(orden_id)
        query = {"_id": oid}
    except errors.InvalidId:
        query = {"_id": int(orden_id)}

    updated = await ordenes_collection.find_one_and_update(
        query,
        {"$set": {"estado": estado}},
        return_document=True
    )
    if not updated:
        raise HTTPException(status_code=404, detail="Orden no encontrada")

    return orden_serializer(updated)

@router.delete("/{orden_id}")
async def delete_orden(orden_id: str):
    query = {}
    try:
        oid = ObjectId(orden_id)
        query = {"_id": oid}
    except errors.InvalidId:
        query = {"_id": int(orden_id)}

    result = await ordenes_collection.delete_one(query)
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Orden no encontrada")
    return {"message": "Orden eliminada correctamente"}
