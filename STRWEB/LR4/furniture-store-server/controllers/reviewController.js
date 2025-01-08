import Review from '../models/Review.js';
import mongoose from 'mongoose';
import { request } from 'express';
import User from "../models/User.js";

export const create = async (req, res) => {
    console.log('--- Requset received ---');
    console.log('Request body:', req.body);
    try {
        const doc = new Review({
            comment: req.body.comment,
            user_id: req.user_id,
            rating: req.body.rating,
        });
        console.log('Document to save:', doc);

        const review = await doc.save();
        console.log('Review saved:', review);

        res.json(review);
    } catch (error) {
        console.error('Error creating review:', error);
        res.status(500).json({ message: 'Error occurred when creating review' });
    }
};

export const getAll = async (req, res) => {
    try {
        const { sort, user_id } = req.query;

        const filter = user_id
            ? { user_id: mongoose.Types.ObjectId(user_id) }
            : {};

        const sortOptions = sort === 'rating_asc' ? { rating: 1 } : sort === 'rating_desc' ? { rating: -1 } : {};
        
        const reviews = await Review.find(filter)
            .populate({ path: 'user_id', model: User })
            .sort(sortOptions)
            .exec();

        res.json(reviews);
    } catch (error) {
        console.error('Error getting reviews:', error);
        res.status(500).json({ message: 'Error occurred when getting reviews' });
    }
};