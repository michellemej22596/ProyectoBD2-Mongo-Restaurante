import streamlit as st
from mongo_connection import get_db

def show_menu():
    db = get_db()

    # Obtener lista de restaurantes
    restaurantes = db.Restaurantes.find()
    restaurante_opciones = [r["nombre"] for r in restaurantes]

    # Selección del restaurante
    selected_restaurante = st.selectbox("Selecciona un restaurante", restaurante_opciones)

    # Filtrar los pedidos de ese restaurante
    pedidos = db.Ordenes.find({"restaurante_nombre": selected_restaurante})
    for pedido in pedidos:
        st.write(f"Pedido: {pedido['_id']}, Total: {pedido['total']}, Estado: {pedido['estado']}")
