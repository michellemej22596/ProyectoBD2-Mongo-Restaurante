const express = require('express');
const mongoose = require('mongoose');
const dotenv = require('dotenv');
const connectDB = require('./config/db');
const restaurantRoutes = require('./routes/restaurantRoutes');
const userRoutes = require('./routes/userRoutes');

dotenv.config(); // Cargar variables de entorno

connectDB();     // Conectar a MongoDB

const app = express();
app.use(express.json());

// Rutas
app.get('/', (req, res) => {
  res.send('API funcionando');
});

app.use('/api/restaurants', restaurantRoutes);
app.use('/api/users', userRoutes);


// Puerto
const PORT = process.env.PORT || 5000;
app.listen(PORT, () => console.log(`Servidor corriendo en puerto ${PORT}`));
