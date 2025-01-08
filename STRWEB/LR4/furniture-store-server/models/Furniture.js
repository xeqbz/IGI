import mongoose from 'mongoose';
import Category from './Category.js';

const furnitureSchema = new mongoose.Schema({
    name: {
        type: String,
        required: [true, 'Name is required'],
        trim: true,
    },
    description: {
        type: String,
    },
    price: {
        type: Number,
        required: [true, 'Price is required'],
        min: [0, 'Price cannot be negative'],
    },
    category: {
        type: mongoose.Schema.Types.ObjectId,
        ref: 'Category',
    },
    imageUrl: {
        type: String,
        required: true,
    },
    stock: {
        type: Number,
        default: 0,
    },
}, {timestamps: true });

export default mongoose.model('Furniture', furnitureSchema);