import streamlit as st
from mongo_connection import get_db

def app():
    st.image("assets/RestaurantesBannerPY2.jpg", caption="Banner Restaurantes", use_container_width=True)
    st.title("📋 Restaurantes Registrados")

    categoria = st.sidebar.radio("Selecciona una sección", options=["SteakHouse", "Vegano", "Vegetarianos"])

    db = get_db()
    restaurantes = db.restaurantes.find({"categoria": categoria})

    if restaurantes.count() == 0:
        st.info(f"📭 No hay restaurantes registrados en la categoría {categoria}.")
    else:
        st.write(f"### Restaurantes en la categoría: {categoria}")
        for restaurante in restaurantes:
            st.write(f"- **{restaurante['nombre']}** – {restaurante['ubicacion']}")
