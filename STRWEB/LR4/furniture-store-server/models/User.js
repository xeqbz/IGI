import mongoose from 'mongoose';
const userSchema = new mongoose.Schema({
    name : {
        type: String,
        required: true
    },
    googleId : {
        type: String,
    },
    role : {
        type: String,
        enum: ['admin', 'client'],
        default: 'client',
        required: true
    },
    email: {
        type: String,
        required: true,
    },
    birthday: {
        type: Date,
    },
    passwordHash: {
        type: String,
    },
    phone: String,
},
{
    timestamps: true
});

const User = mongoose.model("User", userSchema);
export default mongoose.model('User', userSchema);