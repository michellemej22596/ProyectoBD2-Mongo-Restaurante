from pymongo import MongoClient

def get_mongo_connection():
    # Cambia por tu URL de conexión en MongoDB Atlas
    mongo_uri = "mongodb+srv://<usuario>:<contraseña>@cluster0.mongodb.net/?retryWrites=true&w=majority"
    client = MongoClient(mongo_uri)
    return client

def get_db():
    client = get_mongo_connection()
    db = client['Proyecto2']  # Sustituye por el nombre de tu base de datos
    return db
