import streamlit as st
from mongo_connection import get_db

def agregar_restaurante():
    db = get_db()
    
    st.image("assets/RestaurantesBannerPY2.jpg", caption="Banner Restaurantes", use_container_width=True)
    st.write("### ➕ Agregar Nuevo Restaurante")
    
    nombre = st.text_input("Nombre del Restaurante")
    ubicacion = st.text_input("Ubicación")
    categoria = st.selectbox("Categoría", ["SteakHouse", "Vegano", "Vegetarianos"])

    if st.button("Agregar Restaurante"):
        if nombre and ubicacion and categoria:
            db.restaurantes.insert_one({
                "nombre": nombre,
                "ubicacion": ubicacion,
                "categoria": categoria
            })
            st.success(f"✅ Restaurante '{nombre}' agregado correctamente.")
        else:
            st.warning("⚠️ Por favor completa todos los campos.")
