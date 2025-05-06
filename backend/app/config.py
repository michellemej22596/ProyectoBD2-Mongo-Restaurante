from dotenv import load_dotenv
import os

load_dotenv()

class Settings:
    MONGO_URI: str = os.getenv("MONGO_URI", "")

    if not MONGO_URI:
        raise ValueError("MONGO_URI environment variable is required.")

settings = Settings()
