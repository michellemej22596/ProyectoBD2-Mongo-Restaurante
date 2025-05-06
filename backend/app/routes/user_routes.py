# app/routes/user_routes.py
from fastapi import APIRouter
from app.controllers.user_controller import router as user_router

router = APIRouter()

# Eliminar el prefijo '/api' aquí, ya que el prefijo se maneja en main.py
router.include_router(user_router)
