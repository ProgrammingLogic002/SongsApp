import mongoose from 'mongoose';

const favoritoSchema = new mongoose.Schema({
    listaFavoritos: {
        type: mongoose.Schema.Types.ObjectId,
        ref: 'ListaFavoritos',
        required: true
    },
    cancion: {
        type: mongoose.Schema.Types.ObjectId,
        ref: 'Cancion',
        required: true
    },
    posicion: { type: Number, required: true }
}, { timestamps: true });

export const Favorito = mongoose.model('Favorito', favoritoSchema);