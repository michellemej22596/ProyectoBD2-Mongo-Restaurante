from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config import mongodb
from app.routes import user_routes  # Add other routes as needed

app = FastAPI(
    title="Restaurant API",
    description="API para el sistema de gestión de restaurantes",
    version="1.0.0"
)

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup_db_client():
    if not await mongodb.verify_connection():
        raise RuntimeError("Failed to connect to MongoDB")

# Registrar rutas
app.include_router(user_routes.router, prefix="/api", tags=["Usuarios"])
# Add other routes here...

@app.get("/", tags=["Root"])
async def root():
    return {"message": "Bienvenido a la API de Restaurantes"}