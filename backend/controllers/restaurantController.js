const Restaurantes = require('../models/Restaurantes');

// Obtener todos los restaurantes
exports.getRestaurants = async (req, res) => {
  try {
    const restaurants = await Restaurantes.find().populate('menu.item_id', 'nombre precio');
    res.status(200).json(restaurants);
  } catch (error) {
    res.status(500).json({ message: error.message });
  }
};

// Crear un nuevo restaurante
exports.createRestaurant = async (req, res) => {
  const { nombre, direccion, telefono, categoria, menu } = req.body;
  try {
    const newRestaurant = new Restaurantes({ nombre, direccion, telefono, categoria, menu });
    await newRestaurant.save();
    res.status(201).json(newRestaurant);
  } catch (error) {
    res.status(500).json({ message: error.message });
  }
};
