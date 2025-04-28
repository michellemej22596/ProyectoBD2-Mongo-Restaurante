const express = require('express');
const router = express.Router();
const userController = require('../controllers/userController');

// Rutas para los usuarios
router.post('/', userController.createUser);
router.get('/', userController.getUsers);

module.exports = router;
