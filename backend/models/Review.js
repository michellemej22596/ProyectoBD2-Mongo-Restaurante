const mongoose = require('mongoose');

const reviewSchema = new mongoose.Schema({
  user_id: { type: mongoose.Schema.Types.ObjectId, ref: 'User' },
  restaurant_id: { type: mongoose.Schema.Types.ObjectId, ref: 'Restaurant' },
  menu_item_id: { type: mongoose.Schema.Types.ObjectId, ref: 'MenuItem', required: false },
  rating: { type: Number, min: 1, max: 5 },
  comment: String
});

module.exports = mongoose.model('Review', reviewSchema);
