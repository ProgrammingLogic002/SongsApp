import mongoose from 'mongoose';

const cancionSchema = new mongoose.Schema({
    nombre: { type: String, required: true },
    autor: { type: String, required: true },
    portada: { type: String, required: true },
    archivo_audio: { type: String, required: true },
    genero: {
        type: mongoose.Schema.Types.ObjectId,
        ref: 'Genero',
        required: true
    }
}, { timestamps: true });

export const Cancion = mongoose.model('Cancion', cancionSchema);