import mongoose from 'mongoose';
import { Genero } from '../Models/genero.js'; // Ajusta la ruta a tu modelo

const generosIniciales = [
    { nombre: 'Rock' },
    { nombre: 'Pop' },
    { nombre: 'Reggaeton' },
    { nombre: 'Jazz' },
    { nombre: 'Hip Hop' }
];

const sembrarGeneros = async () => {
    try {
    const conn = await mongoose.connect('mongodb://admin:Z%258tKRvh%21UQA4okQ4gnGv%40@localhost:27017/songsapp_db?authSource=admin');
        
        // Inserta los géneros solo si no existen previamente
        for (const genero of generosIniciales) {
            await Genero.updateOne(
                { nombre: genero.nombre }, 
                { $setOnInsert: genero }, 
                { upsert: true }
            );
        }

        console.log('Géneros sembrados correctamente');
        mongoose.connection.close();
    } catch (error) {
        console.error('Error al sembrar géneros:', error);
    }
};

sembrarGeneros();