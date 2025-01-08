import express from 'express';
import jwt from 'jsonwebtoken';
import mongoose, { mongo } from 'mongoose';
import bcrypt from 'bcrypt';
import { validationResult } from 'express-validator';
import { loginValidation, registerValidation } from './validations/auth.js';
import userModel from './models/User.js';
import checkAuth from './utils/checkAuth.js';
import * as UserController from './controllers/userController.js';
import User from './models/User.js';
import * as FurnitureController from './controllers/furnitureController.js';
import { CreateFurnitureValidation } from './validations/furniture.js';
import { checkRole } from './utils/checkRole.js';
import passport from './config/passport.js';
import session from 'express-session';
import './config/passport.js';
import * as ReviewController from './controllers/reviewController.js';
import { CreateReviewValidation } from './validations/review.js';
import cors from 'cors';
import * as CategoryController from './controllers/categoryController.js';

const app = express();
app.use(cors());
app.use(express.json());
app.use(session({ secret: process.env.SESSION_SECRET || 'secret123', resave: false, saveUninitialized: false }));
app.use(passport.initialize());
app.use(passport.session());

mongoose.connect('mongodb+srv://admin:rukil345@cluster-store.nvltp.mongodb.net/store?retryWrites=true&w=majority&appName=Cluster-store', {
    authSource: 'admin',
})
.then(() => console.log('Connected to database'))
.catch((err) => console.log('Db error', err));

app.use(express.json());
app.post('/auth/register', registerValidation, UserController.register);
app.post('/auth/login', loginValidation, UserController.login);
app.get('/auth/me', checkAuth, UserController.getMe);
app.get('/api/users/google', passport.authenticate('google', { scope: ['profile', 'email'] }));
app.get(
    '/api/users/google/callback',
    passport.authenticate('google', { failureRedirect: '/auth/login' }),
    (req, res) => {
        const token = req.user.jwtToken;
        res.redirect(`http://localhost:3000?token=${token}`);
    }
);

app.post('/furniture/create', checkAuth, checkRole(['admin']), CreateFurnitureValidation, FurnitureController.create);
app.get('/furniture', FurnitureController.getAll);
app.get('/furniture/:id', FurnitureController.getOne);
app.delete('/furniture/delete/:id', checkAuth, checkRole(['admin']), CreateFurnitureValidation, FurnitureController.remove);
app.put('/furniture/update/:id', checkAuth, checkRole(['admin']), CreateFurnitureValidation, FurnitureController.update);

app.post('/reviews/create', checkAuth, checkRole(['client', 'admin']), CreateReviewValidation, ReviewController.create);
app.get('/reviews', ReviewController.getAll);

app.get('/categories/all', CategoryController.getCategories);

app.listen(7300, (err) => {
    if (err) {
        return console.log(err);
    }
console.log('Server is running on port 7300');
});