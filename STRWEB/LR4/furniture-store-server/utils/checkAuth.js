import jwt from 'jsonwebtoken';
import { request, response } from 'express';

export default (request, response, next) => {
    const authHeader = request.headers['authorization'];
    console.log('authHeader', authHeader);
    if (!authHeader) {
        return response.status(401).json({ error: 'No token provided' });
    }
    const token = (authHeader).replace(/Bearer\s?/, '');
    if (!token) {
        return response.status(403).json({ error: 'No access' });
    }
    try {
        const decoded = jwt.verify(token, 'secret123');
        request.user_id = decoded._id;
        request.role = decoded.role;
        console.log("Auth OK")
        next();
    } catch (error) {
        console.error(error.message);
        return response.status(401).json({ error: 'Unauthorized' });
    }
};