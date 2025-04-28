# app.py
import streamlit as st
from mongo_connection import get_database

# Configuración de la página
st.set_page_config(page_title="Restaurantes App", layout="wide")

# Título principal
st.title("🍽️ Sistema de Gestión de Restaurantes")

# Menú lateral
page = st.sidebar.selectbox(
    "Selecciona una sección",
    ("Inicio", "Restaurantes", "Menú", "Pedidos", "Reseñas", "Reportes")
)

# Cargar la base de datos
db = get_database()

# Importar páginas
if page == "Inicio":
    st.write("¡Bienvenido a la aplicación de gestión de restaurantes! 🍔🍕🥗")
elif page == "Restaurantes":
    from pages.restaurantes import main
    main(db)
elif page == "Menú":
    from pages.menu import main
    main(db)
elif page == "Pedidos":
    from pages.pedidos import main
    main(db)
elif page == "Reseñas":
    from pages.reseñas import main
    main(db)
elif page == "Reportes":
    from pages.reportes import main
    main(db)
