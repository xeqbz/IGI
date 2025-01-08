import {validationResult} from 'express-validator';
import bcrypt from 'bcrypt';
import userModel from '../models/User.js';
import jwt from 'jsonwebtoken';

export const register = async (req, res) => {
    const errors = validationResult(req);
    if (!errors.isEmpty()) {
        return res.status(400).json(errors.array());
    }
    try {
        const password = req.body.password;
        const salt = await bcrypt.genSalt(10);
        const passwordHash = await bcrypt.hash(password, salt);

        const doc = new userModel({
            name: req.body.name,
            email: req.body.email,
            passwordHash : passwordHash,
            birthday: req.body.birthday,
            phone: req.body.phone,
        });

        const user = await doc.save();
        const { passwordHash: _, ...userWithoutPassword } = user._doc;
        const token = jwt.sign({ _id: user._id }, 'secret123', { expiresIn: '1d' });
        res.json({ ...userWithoutPassword, token });
    } catch (error) {
        console.error('Error registering user:', error);
        return res.status(500).json({ message: 'Error occurred when registering user' });
    }   
};

export const login = async (req, res) => {
    try {
        console.log('Request body:', req.body);
        const user = await userModel.findOne({email: req.body.email});
        if (!user) {
            return res.status(400).json({ message: 'Wrong email or password' });
        }
        const validPassword = await bcrypt.compare(req.body.password, user._doc.passwordHash);
        if (!validPassword) {
            return res.status(400).json({ message: 'Wrong email or password' });
        }
        const { passwordHash: _, ...userWithoutPassword } = user._doc;
        const token = jwt.sign({ _id: user._id, role: user.role}, 'secret123', {expiresIn: '1h'});
        res.json({...userWithoutPassword, token});
    } catch (error) {
        console.error('Error logging in:', error);
        return res.status(500).json({ message: 'Error occurred when logging in' });
    }
};

export const getMe = async (req, res) => {
    try {
        const user = await userModel.findById(req.user_id);
        if (!user) {
            return res.status(404).json({ message: 'User not found' });
        }
        const { passwordHash: _, ...userWithoutPassword } = user._doc;
        res.json(userWithoutPassword);
    } catch (error) {
        console.error('Error getting user:', error);
        return res.status(500).json({ message: 'Error occurred when getting user' });
    }
}