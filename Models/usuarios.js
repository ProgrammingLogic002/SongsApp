import mongoose from 'mongoose';

const usuarioSchema = new mongoose.Schema({
    nombre: { type: String, required: true },
    apodo: { type: String, required: true },
    correo: { type: String, required: true, unique: true },
    contrasena: { type: String, required: true },
    genero: { type: String, required: true },
    foto_perfil: { type: String, required: false }
}, { timestamps: true });

export const Usuario = mongoose.model('Usuario', usuarioSchema);