import mongoose from 'mongoose';

const categorySchema = new mongoose.Schema({
    name: {
        type: String,
        required: [true, 'Category name is required'],
        unique: true,
        trim: true,
    },
    description: {
        type: String,
    },
}, { timestamps: true });

export default mongoose.model('Category', categorySchema);