# main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import asyncio
from app.database import mongodb
from app.routes import restaurante, usuario, menu, resena, orden

app = FastAPI(
    title="API Proyecto 2 - Gestión de Restaurantes",
    description="API para gestión de pedidos y reseñas de restaurantes",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluir routers
app.include_router(restaurante.router, prefix="/restaurantes", tags=["Restaurantes"])
app.include_router(usuario.router, prefix="/usuarios", tags=["Usuarios"])
app.include_router(menu.router, prefix="/menu", tags=["Menu"])
app.include_router(orden.router, prefix="/ordenes", tags=["Ordenes"])
app.include_router(resena.router, prefix="/resenas", tags=["Reseñas"])

# Evento que se ejecuta al iniciar la app para verificar conexión
@app.on_event("startup")
async def startup_db_client():
    is_connected = await mongodb.verify_connection()
    if not is_connected:
        raise Exception("No se pudo conectar a MongoDB Atlas.")

@app.get("/")
async def root():
    return {"message": "API Proyecto 2 - OK"}
