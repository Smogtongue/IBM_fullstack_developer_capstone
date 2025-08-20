/*jshint esversion: 8 */
const mongoose = require('mongoose');
const Schema = mongoose.Schema;

const inventorySchema = new Schema({
  id: {
    type: Number,
    required: true,
  },
  car_make: {
    type: String,
    required: true,
  },
  car_model: {
    type: String,
    required: true,
  },
  car_year: {
    type: Number,
    required: true,
  },
  car_type: {
    type: String,
    required: true,
  },
  car_color: {
    type: String,
    required: true,
  },
  car_mileage: {
    type: Number,
    required: true,
  },
  car_price: {
    type: Number,
    required: true,
  },
  car_condition: {
    type: String,
    required: true,
  },
  dealership: {
    type: Number,
    required: true,
  },
});

module.exports = mongoose.model('inventory', inventorySchema);
