const mongoose = require('mongoose');

const restaurantSchema = new mongoose.Schema({
  nombre: { type: String, required: true },
  direccion: String,
  telefono: String,
  categoria: String,
  menu: [{
    item_id: { type: mongoose.Schema.Types.ObjectId, ref: 'Menu', required: true },
    nombre: String,
    precio: String
  }],
  reseñas: [{
    usuario_id: { type: mongoose.Schema.Types.ObjectId, ref: 'User' },
    calificacion: { type: Number, min: 1, max: 5 },
    comentario: String
  }]
}, { timestamps: true });

// Asegúrate de que el nombre del modelo esté en mayúscula ('Restaurantes')
module.exports = mongoose.model('Restaurantes', restaurantSchema, 'Restaurantes');
