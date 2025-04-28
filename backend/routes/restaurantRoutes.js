const express = require('express');
const router = express.Router();
const restaurantController = require('../controllers/restaurantController');

// Rutas para los restaurantes
router.post('/', restaurantController.createRestaurant);
router.get('/', restaurantController.getRestaurants);

module.exports = router;
