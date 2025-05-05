import streamlit as st
from mongo_connection import get_db

def app():
    db = get_db()

    # Mostrar lista de pedidos
    pedidos = db.pedidos.find()
    st.write("### Lista de Pedidos")
    for pedido in pedidos:
        st.write(f"- Pedido #{pedido['id']} - Restaurante: {pedido['restaurante']} - Total: ${pedido['total']}")
    
    # Formulario para crear un nuevo pedido
    st.write("### Crear Nuevo Pedido")
    restaurante = st.selectbox("Selecciona Restaurante", [r['nombre'] for r in db.restaurantes.find()])
    platillos = [p['nombre'] for p in db.menu.find({"restaurante": restaurante})]
    platillo_seleccionado = st.multiselect("Selecciona los Platillos", platillos)
    total = sum([db.menu.find_one({"nombre": p})['precio'] for p in platillo_seleccionado])
    
    if st.button("Crear Pedido"):
        db.pedidos.insert_one({"restaurante": restaurante, "platillos": platillo_seleccionado, "total": total})
        st.success("Pedido creado correctamente!")
