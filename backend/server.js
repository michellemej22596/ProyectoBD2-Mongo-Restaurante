const express = require('express');
const dotenv = require('dotenv');
const connectDB = require('./config/db');
const restaurantRoutes = require('./routes/restaurantRoutes');
const menuRoutes = require('./routes/menuRoutes');  // Importar las rutas de menú

dotenv.config();  // Cargar las variables de entorno
connectDB();      // Conectar a MongoDB

const app = express();
app.use(express.json());  // Middleware para parsear el cuerpo de las peticiones JSON

app.get('/', (req, res) => {
  res.send('API funcionando');
});

// Rutas
app.use('/api/restaurants', restaurantRoutes);  // Rutas de restaurantes
app.use('/api/menu', menuRoutes);               // Rutas de menú

const PORT = process.env.PORT || 5000;
app.listen(PORT, () => console.log(`Servidor corriendo en puerto ${PORT}`));
