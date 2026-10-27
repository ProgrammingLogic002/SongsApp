import mongoose from 'mongoose';

const generoSchema = new mongoose.Schema({
    nombre: { type: String, required: true }
}, { timestamps: true });

export const Genero = mongoose.model('Genero', generoSchema);