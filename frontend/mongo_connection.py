from pymongo import MongoClient

# Conexion a MongoDB
def get_db():
    uri = "enlace_mongodb_uri" 
    client = MongoClient(uri)
    db = client["Proyecto2"]
    return db