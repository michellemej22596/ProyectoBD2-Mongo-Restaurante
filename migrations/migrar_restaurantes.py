# migrar_restaurantes.py

from pymongo import MongoClient
from bson import ObjectId


MONGO_URI = "mongodb+srv://a:a@cluster0.a67fb.mongodb.net/Proyecto2?retryWrites=true&w=majority&appName=Cluster0"

client = MongoClient(MONGO_URI)
db = client["Proyecto2"]
restaurantes = db.restaurantes

# Buscar todos los documentos antiguos
docs = list(restaurantes.find())

for doc in docs:
    # Crear nuevo documento
    nuevo_doc = {}

    # Nuevo _id como ObjectId
    nuevo_doc["_id"] = ObjectId()

    # Copiar campos
    nuevo_doc["nombre"] = doc.get("nombre", "")
    nuevo_doc["direccion"] = doc.get("direccion", "")
    nuevo_doc["telefono"] = doc.get("telefono", "")
    nuevo_doc["categoria"] = doc.get("categoria", "")
    nuevo_doc["menu"] = doc.get("menu", [])
    nuevo_doc["reseñas"] = doc.get("reseñas", [])

    # Migrar location a GeoJSON
    location = doc.get("location", [])
    if len(location) == 2:
        nuevo_doc["location"] = {
            "type": "Point",
            "coordinates": location
        }
    else:
        nuevo_doc["location"] = {
            "type": "Point",
            "coordinates": [0.0, 0.0]
        }

    # Insertar nuevo documento
    result = restaurantes.insert_one(nuevo_doc)
    print(f"Migrado restaurante {nuevo_doc['nombre']} con nuevo _id {result.inserted_id}")

print("Migración completada.")
