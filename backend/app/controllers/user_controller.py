from fastapi import APIRouter, HTTPException, status
from app.models.user import UserCreate, UserResponse, PyObjectId
from typing import List, Optional, Union
from app.config import database
from bson import ObjectId

router = APIRouter(prefix="/api", tags=["users"])

@router.get("/usuarios", response_model=list[UserResponse])
async def get_usuarios():
    usuarios = await database["Usuarios"].find().to_list(100)
    return [UserResponse(**user) for user in usuarios]

@router.get("/usuarios/{user_id}", response_model=UserResponse)
async def get_usuario(user_id: str):
    try:
        usuario = await database["Usuarios"].find_one({"_id": ObjectId(user_id)})
        if not usuario:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Usuario no encontrado"
            )
        return UserResponse(**usuario)
    except:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="ID inválido"
        )

@router.post("/usuarios", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def create_usuario(user: UserCreate):
    user_dict = user.dict()
    result = await database["Usuarios"].insert_one(user_dict)
    new_user = await database["Usuarios"].find_one({"_id": result.inserted_id})
    return UserResponse(**new_user)

@router.put("/usuarios/{user_id}", response_model=UserResponse)
async def update_usuario(user_id: str, user: UserCreate):
    try:
        user_dict = user.dict()
        result = await database["Usuarios"].update_one(
            {"_id": ObjectId(user_id)},
            {"$set": user_dict}
        )
        if result.matched_count == 0:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Usuario no encontrado"
            )
        updated_user = await database["Usuarios"].find_one({"_id": ObjectId(user_id)})
        return UserResponse(**updated_user)
    except:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="ID inválido"
        )

@router.delete("/usuarios/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_usuario(user_id: str):
    try:
        result = await database["Usuarios"].delete_one({"_id": ObjectId(user_id)})
        if result.deleted_count == 0:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Usuario no encontrado"
            )
    except:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="ID inválido"
        )