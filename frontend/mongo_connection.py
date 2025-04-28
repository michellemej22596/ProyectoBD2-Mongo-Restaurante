from pymongo import MongoClient
import streamlit as st

# Función para conectarse a MongoDB Atlas
@st.cache_resource
def get_database():
    CONNECTION_STRING = "TU_URI_AQUI" # Reemplaza con tu URI de conexión

    client = MongoClient(CONNECTION_STRING)
    return client['restaurantes_db']  # Nombre de la base de datos que se usa
