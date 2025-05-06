# app/routes/restaurant_routes.py
from fastapi import APIRouter
from app.controllers.restaurant_controller import router as restaurant_router

router = APIRouter()

router.include_router(restaurant_router)
