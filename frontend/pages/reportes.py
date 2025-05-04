import plotly.express as px
from mongo_connection import get_db
import pandas as pd
import streamlit as st

def show_reportes():
    db = get_db()

    # Ejemplo de reporte de ventas por restaurante
    ventas = db.Ordenes.aggregate([
        {"$unwind": "$items"},
        {"$group": {
            "_id": "$restaurante_id",
            "total_ventas": {"$sum": {"$multiply": ["$items.precio", "$items.cantidad"]}}
        }},
        {"$sort": {"total_ventas": -1}}
    ])

    ventas = list(ventas)
    df = pd.DataFrame(ventas)

    # Crear gráfico
    fig = px.bar(df, x='_id', y='total_ventas', title="Total de ventas por restaurante")
    st.plotly_chart(fig)
