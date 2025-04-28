const User = require('../models/User');

// Crear un nuevo usuario
exports.createUser = async (req, res) => {
  const { name, email, phone, address } = req.body;
  try {
    const newUser = new User({ name, email, phone, address });
    await newUser.save();
    res.status(201).json(newUser);
  } catch (error) {
    res.status(500).json({ message: error.message });
  }
};

// Obtener todos los usuarios
exports.getUsers = async (req, res) => {
  try {
    const users = await User.find();
    res.status(200).json(users);
  } catch (error) {
    res.status(500).json({ message: error.message });
  }
};
