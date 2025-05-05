import streamlit as st
from mongo_connection import get_db

def app():
    db = get_db()

    # Mostrar lista de menús
    restaurante_nombre = st.selectbox("Selecciona el Restaurante", [r['nombre'] for r in db.restaurantes.find()])
    menu = db.menu.find({"restaurante": restaurante_nombre})
    
    st.write(f"### Menú de {restaurante_nombre}")
    for platillo in menu:
        st.write(f"- {platillo['nombre']} - ${platillo['precio']}")
    
    # Formulario para agregar un nuevo platillo
    st.write("### Agregar Nuevo Platillo")
    platillo_nombre = st.text_input("Nombre del Platillo")
    precio = st.number_input("Precio", min_value=0.0, step=0.01)
    if st.button("Agregar Platillo"):
        db.menu.insert_one({"restaurante": restaurante_nombre, "nombre": platillo_nombre, "precio": precio})
        st.success(f"Platillo '{platillo_nombre}' agregado correctamente!")
