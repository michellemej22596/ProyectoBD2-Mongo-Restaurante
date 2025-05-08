import SectionTitle from '@components/title/SectionTitle.jsx';
import MenuItem from '@components/menu/MenuItem.jsx';
import { useEffect, useState } from 'react';
import api from '../../api'; 
import './menu.css';

const Menu = () => {
  const [menuItems, setMenuItems] = useState([]);  
  const [error, setError] = useState(null);  

  useEffect(() => {
    const fetchMenu = async () => {
      try {
        const response = await api.get('https://proyectobd2-mongo-restaurante.onrender.com/menu/', {
          params: {
            skip: 0,
            limit: 100,
            precio_min: 0,
            precio_max: 10000
          }
        });

        console.log('Respuesta de la API:', response.data); 

        if (Array.isArray(response.data)) {
          setMenuItems(response.data); 
        } else {
          setError('La respuesta de la API no es un arreglo');
        }
      } catch (error) {
        console.error('Error al cargar los platillos:', error);
        setError('Hubo un error al cargar los platillos');
      }
    };

    fetchMenu();
  }, []);

  return (
    <section className='menu section'>
      <div className='container'>
        <div className='menu-header'>
          <SectionTitle
            subtitle='Our Menu'
            title={<>Let's check <span> our menu </span></>}
          />
        </div>

        <div className='menu-container grid'>
          {error && <p>{error}</p>}
          {menuItems.length === 0 && !error ? (
            <p>No items available</p>
          ) : (
            menuItems.map(item => (
              <MenuItem 
                key={item._id} 
                id={item._id} 
                nombre={item.nombre} 
                descripcion={item.descripcion} 
                precio={item.precio} 
                restaurante_id={item.restaurante_id} 
              />
            ))
          )}
        </div>
      </div>
    </section>
  );
};

export default Menu;
