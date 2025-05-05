import streamlit as st
from mongo_connection import get_db

def app():
    db = get_db()

    # Generar reporte de pedidos
    st.write("### Reporte de Pedidos por Restaurante")
    restaurante_nombre = st.selectbox("Selecciona Restaurante", [r['nombre'] for r in db.restaurantes.find()])
    pedidos = db.pedidos.find({"restaurante": restaurante_nombre})

    total_pedidos = 0
    total_ingresos = 0
    for pedido in pedidos:
        total_pedidos += 1
        total_ingresos += pedido['total']

    st.write(f"Total de pedidos: {total_pedidos}")
    st.write(f"Ingresos totales: ${total_ingresos}")
