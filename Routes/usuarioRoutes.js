import { Router } from 'express';
import { crearUsuario } from '../Controllers/AuthController.js';
import { IniciarSesion } from '../Controllers/AuthController.js';

const router = Router();

router.post('/', crearUsuario);

router.post('/login', IniciarSesion);

export default router;
