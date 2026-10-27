import mongoose from 'mongoose';

const listaFavoritosSchema = new mongoose.Schema({
    usuario: {
        type: mongoose.Schema.Types.ObjectId,
        ref: 'Usuario',
        required: true
    },
    portada: { type: String, required: true }
}, { timestamps: true });

export const ListaFavoritos = mongoose.model('ListaFavoritos', listaFavoritosSchema);
