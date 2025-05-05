# app/controllers/user_controller.py
from fastapi import APIRouter, HTTPException
from app.models.user import UserCreate, UserResponse
from app.config import database
from bson import ObjectId

router = APIRouter()

# Ruta para obtener todos los usuarios
@router.get("/usuarios", response_model=list[UserResponse])
async def get_usuarios():
    usuarios = await database["usuarios"].find().to_list(100)  # Limita a los primeros 100
    return usuarios

# Ruta para obtener un usuario por ID
@router.get("/usuario/{user_id}", response_model=UserResponse)
async def get_usuario(user_id: str):
    usuario = await database["usuarios"].find_one({"_id": ObjectId(user_id)})
    if usuario is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usuario

# Ruta para crear un nuevo usuario
@router.post("/usuario", response_model=UserResponse)
async def create_usuario(user: UserCreate):
    user_dict = user.dict()
    result = await database["usuarios"].insert_one(user_dict)
    user_dict["_id"] = result.inserted_id
    return user_dict

# Ruta para actualizar un usuario
@router.put("/usuario/{user_id}", response_model=UserResponse)
async def update_usuario(user_id: str, user: UserCreate):
    user_dict = user.dict()
    result = await database["usuarios"].update_one({"_id": ObjectId(user_id)}, {"$set": user_dict})
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return {**user_dict, "_id": user_id}

# Ruta para eliminar un usuario
@router.delete("/usuario/{user_id}", status_code=204)
async def delete_usuario(user_id: str):
    result = await database["usuarios"].delete_one({"_id": ObjectId(user_id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
