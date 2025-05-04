import streamlit as st
from mongo_connection import connect_to_mongo

def app():
    db = connect_to_mongo()

    # Mostrar reseñas
    restaurante_nombre = st.selectbox("Selecciona Restaurante", [r['nombre'] for r in db.restaurantes.find()])
    reseñas = db.reseñas.find({"restaurante": restaurante_nombre})
    
    st.write(f"### Reseñas de {restaurante_nombre}")
    for reseña in reseñas:
        st.write(f"- {reseña['comentario']} - Calificación: {reseña['calificacion']}")
    
    # Formulario para agregar una reseña
    st.write("### Agregar Reseña")
    comentario = st.text_area("Comentario")
    calificacion = st.slider("Calificación", 1, 5)
    if st.button("Agregar Reseña"):
        db.reseñas.insert_one({"restaurante": restaurante_nombre, "comentario": comentario, "calificacion": calificacion})
        st.success("Reseña agregada correctamente!")