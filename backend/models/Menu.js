const mongoose = require('mongoose');

const menuSchema = new mongoose.Schema({
  nombre: { type: String, required: true },
  descripcion: String,
  precio: { type: String, required: true },  // El precio está como String en la base de datos
  restaurante_id: { type: mongoose.Schema.Types.ObjectId, ref: 'Restaurantes', required: true }  // Referencia al Restaurante
}, { timestamps: true });

module.exports = mongoose.model('Menu', menuSchema, 'Menu');  // 'Menu' es el nombre de la colección en la base de datos
