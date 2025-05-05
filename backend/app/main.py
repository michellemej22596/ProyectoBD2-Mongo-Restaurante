# app/main.py
from fastapi import FastAPI
from app.routes.user_routes import router as user_routes

app = FastAPI()

# Registrar las rutas
app.include_router(user_routes)

@app.get("/")
def read_root():
    return {"message": "Welcome to the restaurant API"}
