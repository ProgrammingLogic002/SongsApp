import express from 'express';
import { connectDB } from '../config/db.js';
import usuarioRoutes from '../Routes/usuarioRoutes.js';
import cancionesRoutes from '../Routes/cancionesRoute.js';
import favoritosRoutes from '../Routes/favoritoRoute.js';

const app = express();

app.use(express.json());

connectDB();

app.use('/api/usuarios', usuarioRoutes);
app.use('/api/canciones', cancionesRoutes);
app.use('/api/favoritos', favoritosRoutes);


const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Servidor corriendo en el puerto ${PORT}`);
});