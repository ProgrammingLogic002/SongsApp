import {Usuario} from '../Models/usuarios.js';

export const crearUsuario = async (req, res) => {
    try {
        const { nombre, apodo, correo, contrasena, genero } = req.body;

        if (!nombre || !apodo || !correo || !contrasena || !genero) {
            return res.status(400).json({ error: 'Todos los campos son obligatorios' });
        }

        const nuevoUsuario = new Usuario({
            nombre,
            apodo,
            correo,
            contrasena,
            genero
        });
        await nuevoUsuario.save();
        res.status(201).json({ message: 'Usuario creado correctamente', usuario: nuevoUsuario });
    } catch (error) {
        console.error('Error al crear el usuario:', error);
        res.status(500).json({ error: 'Error al crear el usuario' });
    }
}

export const IniciarSesion = async (req, res) => {
    try {
        const { correo, contrasena } = req.body;

        if (!correo || !contrasena) {
            return res.status(400).json({ error: 'Correo y contraseña son obligatorios' });
        }

        const usuario = await Usuario.findOne({ correo });
        if (!usuario) {
            return res.status(404).json({ error: 'Usuario no encontrado' });
        }

        if (usuario.contrasena !== contrasena) {
            return res.status(401).json({ error: 'Contraseña incorrecta' });
        }
        
        res.status(200).json({ message: 'Inicio de sesión exitoso', usuario });
    } catch (error) {
        console.error('Error al iniciar sesión:', error);
        res.status(500).json({ error: 'Error al iniciar sesión' });
    }
    
}