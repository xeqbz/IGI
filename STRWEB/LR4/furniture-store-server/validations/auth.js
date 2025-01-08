import { body } from 'express-validator';

export const registerValidation = [
    body('email').isEmail().withMessage('Invalid email'),
    body('password').isLength({ min: 6 }).withMessage('Password must be at least 6 characters long'),
    body('name').isLength({ min: 3 }).withMessage('Name must be at least 3 characters long'),
    body('birthday').isDate().withMessage('Invalid date'),
    body('phoen').optional()
                        .matches(/^\+375(25|29|33|44|17)\d{7}$/)
                        .withMessage('Please enter a valid phone number in the format +375XXXXXXXXX'),
];

export const loginValidation = [
    body('email').isEmail().withMessage('Invalid email'),
    body('password').isLength({ min: 6 }).withMessage('Password must be at least 6 characters long'),
];