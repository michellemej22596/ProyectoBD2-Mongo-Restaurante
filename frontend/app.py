import streamlit as st

st.title("Gestión de Restaurantes")

#Navegación entre páginas
PAGES = {
    "Restaurantes": "restaurantes",
    "Menú": "menu",
    "Pedidos": "pedidos",
    "Reseñas": "review",
    "Reportes": "reportes",
}

page = st.sidebar.radio("Selecciona una sección", options=list(PAGES.keys()))
st.write(f"## {page}")
# Cargar el script de la página correspondiente
if page == "Restaurantes":
    from pages.restaurantes import app
elif page == "Menú":
    from pages.menu import app
elif page == "Pedidos":
    from pages.pedidos import app
elif page == "Reseñas":
    from pages.review import app
elif page == "Reportes":
    from pages.reportes import app

app()
