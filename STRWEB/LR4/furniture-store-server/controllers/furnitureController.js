import FurnitureModel from '../models/Furniture.js';
import mongoose from 'mongoose';
import Furniture from '../models/Furniture.js';

export const create = async (req, res) => {
    console.log('--- Request received ---');
    console.log('Request body:', req.body);
    try {
        const doc = new FurnitureModel({
            name: req.body.name,
            description: req.body.description,
            price: req.body.price,
            category: req.body.category,
            imageUrl: req.body.imageUrl,
            stock: req.body.stock,
        });
        console.log('Document to be saved:', doc);
        const furniture = await doc.save();
        console.log('Saved product:', furniture);
        res.json(furniture);
    } catch (error) {
        console.error('Error creating product:', error);
        res.status(500).json({ message: "Error occured when creating product" });
    }
};

export const getAll = async (req, res) => {
    try {
        const { name, sort } = req.query;

        const filter = name
            ? { name: { $regex: new RegExp(name, '1')}}
            : {};

        const sortOptions = sort === 'price_asc' ? { price: 1 } : sort === 'price_desc' ? { price: -1 } : {};

        const furniture = await FurnitureModel.find(filter)
            .populate('category')
            .sort(sortOptions)
            .exec();
        
        res.json(furniture);
    } catch (error) {
        console.error('Error fetching furniture:', error);
        res.status(500).json({ message: "Error occured when fetching furniture" });
    }
};

export const getOne = async (req, res) => {
    try {
        const furnitureId = req.params.id;
        if (!mongoose.Types.ObjectId.isValid(furnitureId)) {
            return res.status(400).json({ message: "Invalid furniture ID" });
        }

        const furniture = await FurnitureModel.findById(furnitureId).populate('category').exec();

        if(!furniture) {
            return res.status(404).json({ message: "Furniture not found" });
        }

        res.json(furniture);
    } catch (error) {
        console.log(error);
        res.status(400).json({ message: "Could not get the furniture" });
    }
};

export const update = async (req, res) => {
    try {
        const furnitureId = req.params.id;

        const furniture = await FurnitureModel.findById(furnitureId);
        if (!furniture) {
            return res.status(404).json({ message: "Furniture not found" });
        }

        const updatedFurniture = await FurnitureModel.findByIdAndUpdate(
            furnitureId,
            {
                name: req.body.name || furniture.name,
                description: req.body.description || furniture.description,
                price: req.body.price || furniture.price,
                category: req.body.category || furniture.category,
                imageUrl: req.body.imageUrl || furniture.imageUrl,
                stock: req.body.stock || furniture.stock,
            },
            { new: true }
        );

        res.json(updatedFurniture);
    } catch (error) {
        console.log(error);
        res.status(500).json({ message: "Could not update the furniture" });
    }
};

export const remove = async (req, res) => {
    try {
        const furnitureId = req.params.id;
        console.log("Received ID on server:", req.params.id);

        if (!mongoose.Types.ObjectId.isValid(furnitureId)) {
            return res.status(400).json({ message: "Invalid furniture ID" });
        }

        const deletedFurniture = await FurnitureModel.findOneAndDelete({ _id: furnitureId });

        if (!deletedFurniture) {
            return res.status(404).json({ message: "Furniture not found" });
        }

        res.json({
            success: true,
            message: "Furniture deleted successfully",
        });
    } catch (error) {
        console.log(error);
        res.status(500).json({ message: "Could not delete the furniture" });
    }
};