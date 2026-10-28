import express from 'express';
import { connectDB } from '../config/db.js';
import usuarioRoutes from '../Routes/usuarioRoutes.js';

const app = express();

app.use(express.json());

connectDB();

app.use('/api/usuarios', usuarioRoutes);


const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Servidor corriendo en el puerto ${PORT}`);
});