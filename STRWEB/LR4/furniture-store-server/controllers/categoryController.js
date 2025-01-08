import mongoose from 'mongoose';
import Category from '../models/Category.js';

export const getCategories = async (req, res) => {
    try {
        const categories = await Category.find();

        res.status(200).json(categories);
    } catch (error) {
        console.error("Error fetching categories: ", error);
        res.status(500).json({ message: "Error fetching categories", error: error.message, });
    }
};