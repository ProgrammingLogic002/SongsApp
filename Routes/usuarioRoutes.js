import { Router } from 'express';
import multer from 'multer';
import path from 'path';
import { crearUsuario } from '../Controllers/AuthController.js';
import { IniciarSesion } from '../Controllers/AuthController.js';
import { actualizarUsuario } from '../Controllers/UsuarioController.js';
import { cambiarCorreo } from '../Controllers/UsuarioController.js';
import { cambiarContrasena } from '../Controllers/UsuarioController.js';
import { subirFotoPerfil } from '../Controllers/UsuarioController.js';
import { eliminarCuenta } from '../Controllers/UsuarioController.js';

const router = Router();

const storage = multer.diskStorage({
    destination: function (req, file, cb) {
        cb(null, 'uploads/') 
    },
    filename: function (req, file, cb) {
        cb(null, Date.now() + path.extname(file.originalname));
    }
});

const upload = multer({ storage: storage });

router.post('/', crearUsuario);

router.post('/login', IniciarSesion);

router.put('/:id', actualizarUsuario);

router.patch('/:id/foto', upload.single('foto'), subirFotoPerfil);

router.patch('/:id/correo', cambiarCorreo);

router.patch('/:id/contrasena', cambiarContrasena);

router.delete('/:id', eliminarCuenta);

export default router;
