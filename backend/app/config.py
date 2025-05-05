# app/config.py
import motor.motor_asyncio
from dotenv import load_dotenv
import os

# Cargar variables de entorno desde el archivo .env
load_dotenv()

# Obtener la URI de MongoDB desde el archivo .env
MONGO_URI = os.getenv("MONGO_URI")

# Conexión a la base de datos MongoDB usando Motor
client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URI)
database = client.get_database()  # Por defecto se conecta a la base de datos especificada en la URI
