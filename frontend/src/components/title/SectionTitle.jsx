import { RiAddBoxFill } from "react-icons/ri";
import { useState } from "react";
import "./sectionTitle.css";
import axios from "axios";

const SectionTitle = ({ subtitle, title, onDishCreated }) => {
  const [isFormVisible, setIsFormVisible] = useState(false);
  const [newDish, setNewDish] = useState({
    nombre: "",
    descripcion: "",
    precio: "",
    restaurante_id: ""
  });

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setNewDish({
      ...newDish,
      [name]: value
    });
  };

  const handleCreateDish = async (e) => {
    e.preventDefault();

    try {
      const response = await axios.post("https://proyectobd2-mongo-restaurante.onrender.com/menu/", newDish, {
        headers: {
          "Content-Type": "application/json"
        }
      });

      if (response.status === 200) {
        alert("Platillo creado con éxito!");
        setIsFormVisible(false);
        setNewDish({
          nombre: "",
          descripcion: "",
          precio: "",
          restaurante_id: ""
        });
        if (onDishCreated) onDishCreated(); // Notifica al padre
      }
    } catch (error) {
      console.error("Error al crear el platillo", error);
      alert("Hubo un error al crear el platillo");
    }
  };

  return (
    <div>
      <span className="section-subtitle">{subtitle}</span>
      <div className="section-title-container">
        <h2 className="section-title">{title}</h2>
        <RiAddBoxFill
          className="add-icon"
          onClick={() => setIsFormVisible(!isFormVisible)}
        />
      </div>

      {isFormVisible && (
        <div className="form-wrapper">
          <form onSubmit={handleCreateDish} className="create-dish-form">
            <input
              type="text"
              name="nombre"
              placeholder="Nombre"
              value={newDish.nombre}
              onChange={handleInputChange}
              required
            />
            <input
              type="text"
              name="descripcion"
              placeholder="Descripción"
              value={newDish.descripcion}
              onChange={handleInputChange}
              required
            />
            <input
              type="number"
              name="precio"
              placeholder="Precio"
              value={newDish.precio}
              onChange={handleInputChange}
              required
            />
            <input
              type="text"
              name="restaurante_id"
              placeholder="ID del restaurante"
              value={newDish.restaurante_id}
              onChange={handleInputChange}
              required
            />
            <button type="submit">Crear Platillo</button>
          </form>
        </div>
      )}
    </div>
  );
};

export default SectionTitle;
