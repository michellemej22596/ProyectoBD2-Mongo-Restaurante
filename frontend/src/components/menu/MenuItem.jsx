import React from 'react';

const MenuItem = ({ id, nombre, descripcion, precio, restaurante_id }) => {
  return (
    <div className="menu-item">
      <p className="menu-id">ID: {id}</p>
      <h3 className="menu-name">{nombre}</h3>
      <p className="menu-description">{descripcion}</p>
      <div className="menu-price">Price: {precio}</div>
      <div className="menu-restaurant-id">Restaurant ID: {restaurante_id}</div>
    </div>
  );
};

export default MenuItem;
