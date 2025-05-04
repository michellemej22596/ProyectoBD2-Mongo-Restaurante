import streamlit as st
from mongo_connection import connect_to_mongo

def app():
    db = connect_to_mongo()

    # Mostrar lista de restaurantes
    restaurantes = db.restaurantes.find()
    st.write("### Lista de Restaurantes")
    for restaurante in restaurantes:
        st.write(f"- {restaurante['nombre']} - {restaurante['ubicacion']}")
    
    # Formulario para agregar un nuevo restaurante
    st.write("### Agregar Nuevo Restaurante")
    nombre = st.text_input("Nombre del Restaurante")
    ubicacion = st.text_input("Ubicación")
    if st.button("Agregar Restaurante"):
        db.restaurantes.insert_one({"nombre": nombre, "ubicacion": ubicacion})
        st.success(f"Restaurante '{nombre}' agregado correctamente!")
