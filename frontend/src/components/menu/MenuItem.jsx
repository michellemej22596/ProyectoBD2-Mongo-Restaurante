import React, { useState } from 'react';
import { MdEdit } from 'react-icons/md';

const MenuItem = ({ id, nombre, descripcion, precio, restaurante_id }) => {
  const [isEditing, setIsEditing] = useState(false);
  const [editData, setEditData] = useState({
    nombre,
    descripcion,
    precio: parseFloat(precio).toFixed(2), // lo formateas como string con 2 decimales
    restaurante_id
  });

  const handleChange = (e) => {
    setEditData({ ...editData, [e.target.name]: e.target.value });
  };

  const handleSave = async () => {
    try {
      const parsedPrecio = parseFloat(parseFloat(editData.precio).toFixed(2)); // fuerza redondeo

      const response = await fetch(`https://proyectobd2-mongo-restaurante.onrender.com/menu/${id}`, {
        method: 'PUT',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          nombre: editData.nombre,
          descripcion: editData.descripcion,
          precio: parsedPrecio,
          restaurante_id: editData.restaurante_id
        })
      });

      if (!response.ok) throw new Error('Error en la actualización');

      const data = await response.json();
      console.log('Platillo actualizado:', data);
      setEditData(prev => ({ ...prev, precio: parsedPrecio.toFixed(2) })); 
      setIsEditing(false);
    } catch (err) {
      console.error('Error al actualizar:', err);
    }
  };

  return (
    <div className="menu-item">
      <div className="menu-header">
        <p className="menu-id">ID: {id}</p>
        <MdEdit onClick={() => setIsEditing(!isEditing)} style={{ cursor: 'pointer', marginLeft: '8px' }} />
      </div>

      {isEditing ? (
        <>
          <input type="text" name="nombre" value={editData.nombre} onChange={handleChange} />
          <input type="text" name="descripcion" value={editData.descripcion} onChange={handleChange} />
          <input type="number" name="precio" value={editData.precio} onChange={handleChange} step="0.01" />
          <button onClick={handleSave}>Guardar</button>
        </>
      ) : (
        <>
          <h3 className="menu-name">{nombre}</h3>
          <p className="menu-description">{descripcion}</p>
          <div className="menu-price">Price: Q{parseFloat(precio).toFixed(2)}</div>
          <div className="menu-restaurant-id">Restaurant ID: {restaurante_id}</div>
        </>
      )}
    </div>
  );
};

export default MenuItem;
