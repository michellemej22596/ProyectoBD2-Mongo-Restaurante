# routes/usuario.py

from fastapi import APIRouter, HTTPException
from app.models.usuario import UsuarioIn, UsuarioOut, UsuarioUpdate
from app.database import mongodb
from bson import ObjectId, errors
from typing import List

router = APIRouter()

usuarios_collection = mongodb.get_db()["Usuarios"]

def usuario_serializer(doc):
    doc["_id"] = str(doc["_id"])
    return doc

@router.get("/", response_model=List[UsuarioOut])
async def get_usuarios():
    usuarios = await usuarios_collection.find().to_list(100)
    return [usuario_serializer(u) for u in usuarios]

@router.get("/{usuario_id}", response_model=UsuarioOut)
async def get_usuario(usuario_id: str):
    query = {}

    try:
        # Intentar como ObjectId
        oid = ObjectId(usuario_id)
        query = {"_id": oid}
    except errors.InvalidId:
        # Si no es ObjectId → usar como entero si es posible, o como string
        try:
            query = {"_id": int(usuario_id)}
        except ValueError:
            query = {"_id": usuario_id}

    usuario = await usuarios_collection.find_one(query)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    return usuario_serializer(usuario)

@router.post("/", response_model=UsuarioOut)
async def create_usuario(usuario: UsuarioIn):
    res = await usuarios_collection.insert_one(usuario.dict())
    new_usuario = await usuarios_collection.find_one({"_id": res.inserted_id})
    return usuario_serializer(new_usuario)

@router.put("/{usuario_id}", response_model=UsuarioOut)
async def update_usuario(usuario_id: str, usuario: UsuarioUpdate):
    query = {}

    try:
        oid = ObjectId(usuario_id)
        query = {"_id": oid}
    except errors.InvalidId:
        try:
            query = {"_id": int(usuario_id)}
        except ValueError:
            query = {"_id": usuario_id}

    updated = await usuarios_collection.find_one_and_update(
        query,
        {"$set": {k: v for k, v in usuario.dict(exclude_none=True).items()}},
        return_document=True
    )
    if not updated:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usuario_serializer(updated)

@router.delete("/{usuario_id}")
async def delete_usuario(usuario_id: str):
    query = {}

    try:
        oid = ObjectId(usuario_id)
        query = {"_id": oid}
    except errors.InvalidId:
        try:
            query = {"_id": int(usuario_id)}
        except ValueError:
            query = {"_id": usuario_id}

    result = await usuarios_collection.delete_one(query)
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return {"message": "Usuario eliminado correctamente"}
