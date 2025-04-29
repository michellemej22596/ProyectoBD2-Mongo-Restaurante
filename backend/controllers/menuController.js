const Menu = require('../models/Menu');

// Obtener todos los platillos del menú
exports.getMenuItems = async (req, res) => {
  try {
    const menuItems = await Menu.find().populate('restaurante_id', 'nombre direccion');  // Obtener restaurante relacionado
    res.status(200).json(menuItems);  // Devolver todos los platillos
  } catch (error) {
    res.status(500).json({ message: error.message });
  }
};

// Crear un nuevo platillo en el menú
exports.createMenuItem = async (req, res) => {
  const { nombre, descripcion, precio, restaurante_id } = req.body;

  try {
    const newMenuItem = new Menu({ nombre, descripcion, precio, restaurante_id });
    await newMenuItem.save();
    res.status(201).json(newMenuItem);  // Devolver el nuevo platillo creado
  } catch (error) {
    res.status(500).json({ message: error.message });
  }
};

// Obtener un platillo específico del menú
exports.getMenuItemById = async (req, res) => {
  try {
    const menuItem = await Menu.findById(req.params.id).populate('restaurante_id', 'nombre direccion');
    if (!menuItem) {
      return res.status(404).json({ message: 'Platillo no encontrado' });
    }
    res.status(200).json(menuItem);
  } catch (error) {
    res.status(500).json({ message: error.message });
  }
};

// Actualizar un platillo en el menú
exports.updateMenuItem = async (req, res) => {
  try {
    const updatedMenuItem = await Menu.findByIdAndUpdate(req.params.id, req.body, { new: true });
    if (!updatedMenuItem) {
      return res.status(404).json({ message: 'Platillo no encontrado' });
    }
    res.status(200).json(updatedMenuItem);
  } catch (error) {
    res.status(500).json({ message: error.message });
  }
};

// Eliminar un platillo en el menú
exports.deleteMenuItem = async (req, res) => {
  try {
    const deletedMenuItem = await Menu.findByIdAndDelete(req.params.id);
    if (!deletedMenuItem) {
      return res.status(404).json({ message: 'Platillo no encontrado' });
    }
    res.status(200).json({ message: 'Platillo eliminado' });
  } catch (error) {
    res.status(500).json({ message: error.message });
  }
};
