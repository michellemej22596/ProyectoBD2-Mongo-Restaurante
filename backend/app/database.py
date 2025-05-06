import motor.motor_asyncio
from pymongo.errors import ConnectionFailure
from app.config import settings

class MongoDB:
    def __init__(self):
        self.client = motor.motor_asyncio.AsyncIOMotorClient(
            settings.MONGO_URI,
            serverSelectionTimeoutMS=5000,  # Tiempo máximo para intentar conexión (5s)
            connectTimeoutMS=5000
        )

    async def verify_connection(self):
        try:
            await self.client.admin.command("ping")
            print("✅ Conexión exitosa a MongoDB Atlas")
            return True
        except ConnectionFailure as e:
            print(f"❌ Error de conexión a MongoDB: {e}")
            return False

    def get_db(self, db_name: str = "Proyecto2"):
        return self.client[db_name]

mongodb = MongoDB()
database = mongodb.get_db()
