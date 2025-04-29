const express = require('express');
const router = express.Router();
const menuController = require('../controllers/menuController');

// Rutas para los platillos del menú
router.get('/', menuController.getMenuItems);        // Obtener todos los platillos
router.post('/', menuController.createMenuItem);     // Crear un platillo
router.get('/:id', menuController.getMenuItemById);  // Obtener un platillo por ID
router.put('/:id', menuController.updateMenuItem);   // Actualizar un platillo
router.delete('/:id', menuController.deleteMenuItem); // Eliminar un platillo

module.exports = router;
