import streamlit as st
from pages import restaurantes, menu, pedidos, reseñas, reportes

st.title("Gestión de Restaurantes")

page = st.sidebar.selectbox("Selecciona una sección", ["Restaurantes", "Menú", "Pedidos", "Reseñas", "Reportes"])

if page == "Restaurantes":
    restaurantes.show_restaurantes()
elif page == "Menú":
    menu.show_menu()
elif page == "Pedidos":
    pedidos.show_pedidos()
elif page == "Reseñas":
    reseñas.show_reseñas()
elif page == "Reportes":
    reportes.show_reportes()
