import motor.motor_asyncio
from dotenv import load_dotenv
import os
from pymongo.errors import ConnectionFailure

# Cargar variables de entorno
load_dotenv()

class MongoDB:
    def __init__(self):
        self.MONGO_URI = os.getenv("MONGO_URI")
        if not self.MONGO_URI:
            raise ValueError("MONGO_URI environment variable not set")

        # Conexión a MongoDB Atlas
        self.client = motor.motor_asyncio.AsyncIOMotorClient(self.MONGO_URI)

    async def verify_connection(self):
        try:
            await self.client.admin.command('ping')
            print("✅ Successfully connected to MongoDB Atlas!")
            return True
        except Exception as e:
            print(f"❌ Could not connect to MongoDB: {e}")
            return False

    def get_db(self, db_name="Proyecto2"):
        return self.client[db_name]

# Instancia global de la conexión
mongodb = MongoDB()
database = mongodb.get_db()