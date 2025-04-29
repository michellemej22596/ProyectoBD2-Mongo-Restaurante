const mongoose = require('mongoose');

const orderSchema = new mongoose.Schema({
  user_id: { type: mongoose.Schema.Types.ObjectId, ref: 'User' },
  items: [{
    menu_item_id: { type: mongoose.Schema.Types.ObjectId, ref: 'Menu' },
    quantity: Number,
    price: Number
  }],
  total: Number,
  status: { type: String, enum: ['pending', 'in_progress', 'completed'] },
  date: { type: Date, default: Date.now }
});

module.exports = mongoose.model('Order', orderSchema);
