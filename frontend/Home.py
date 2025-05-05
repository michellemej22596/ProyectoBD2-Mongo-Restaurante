import streamlit as st
from pages import Restaurantes, Menu, Pedidos, Review, Reportes
from controllerPages import RestauranteController  # <-- Asegúrate de importar

# Configuración de la página
st.set_page_config(
    page_title="Inicio",
    page_icon="🏠",
    layout="wide"
)

# Barra lateral con las opciones de menú
page = st.sidebar.radio("Selecciona una sección", options=["Inicio", "Restaurantes", "Menú", "Pedidos", "Reseñas", "Reportes"])

# Contenido según la sección seleccionada
if page == "Inicio":
    st.image("assets/HomeBannerPY2.jpg", caption="Imagen de Bienvenida", use_container_width=True)
    st.title("🏠 Gestión de Restaurantes")
    st.write("### Bienvenido al sistema de gestión de restaurantes!")
    st.write("Aquí podrás gestionar tu restaurante, agregar menús, realizar pedidos y mucho más.")

elif page == "Restaurantes":
    RestauranteController.agregar_restaurante()


elif page == "Menú":
    Menu.app()

elif page == "Pedidos":
    Pedidos.app()

elif page == "Reseñas":
    Review.app()

elif page == "Reportes":
    Reportes.app()
