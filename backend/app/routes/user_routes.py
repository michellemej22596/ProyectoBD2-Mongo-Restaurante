# app/routes/user_routes.py
from fastapi import APIRouter
from app.controllers.user_controller import router as user_router

router = APIRouter()

router.include_router(user_router, prefix="/usuarios", tags=["usuarios"])
