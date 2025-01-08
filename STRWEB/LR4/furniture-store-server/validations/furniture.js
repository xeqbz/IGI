import { body } from 'express-validator';

export const CreateFurnitureValidation = [
    body('name').isString().withMessage('Please enter a valid name'),
    body('description').isString().withMessage('Please enter a valid description'),
    body('price').isFloat().withMessage('Please enter a valid price'),
    body('category').isString().withMessage('Please enter a valid category'),
    body('imageUrl').isURL().optional().withMessage('Please enter a valid image URL'),
    body('stock').isInt().withMessage('Please enter a valid quantity'),
];