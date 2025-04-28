const Restaurant = require('../models/Restaurant');

// Crear un nuevo restaurante
exports.createRestaurant = async (req, res) => {
  const { name, address, phone, category } = req.body;
  try {
    const newRestaurant = new Restaurant({ name, address, phone, category });
    await newRestaurant.save();
    res.status(201).json(newRestaurant);
  } catch (error) {
    res.status(500).json({ message: error.message });
  }
};

// Obtener todos los restaurantes
exports.getRestaurants = async (req, res) => {
  try {
    const restaurants = await Restaurant.find();
    res.status(200).json(restaurants);
  } catch (error) {
    res.status(500).json({ message: error.message });
  }
};
