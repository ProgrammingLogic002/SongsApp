import {Usuario} from '../Models/usuarios.js';
import bcrypt from 'bcrypt';

export const actualizarUsuario = async (req, res) => {
    try {
        const { id } = req.params;
        const { nombre, apodo } = req.body;

        const usuarioActualizado = await Usuario.findByIdAndUpdate(
            id, 
            { nombre, apodo }, 
            { new: true, runValidators: true } 
        );

        if (!usuarioActualizado) {
            return res.status(404).json({ error: 'Usuario no encontrado' });
        }

        res.status(200).json({ 
            message: 'Perfil actualizado correctamente', 
            usuario: usuarioActualizado 
        });

    } catch (error) {
        console.error('Error al actualizar el usuario:', error);
        res.status(500).json({ error: 'Error al actualizar el usuario' });
    }
}

export const cambiarCorreo = async (req, res) => {
    try {
        const { id } = req.params;
        const { nuevoCorreo } = req.body;

        if (!nuevoCorreo) {
            return res.status(400).json({ error: 'El nuevo correo es obligatorio' });
        }

        const correoEnUso = await Usuario.findOne({ correo: nuevoCorreo });
        if (correoEnUso) {
            return res.status(400).json({ error: 'Este correo ya está registrado por otro usuario' });
        }

        const usuarioActualizado = await Usuario.findByIdAndUpdate(
            id, 
            { correo: nuevoCorreo }, 
            { new: true, runValidators: true } 
        );

        if (!usuarioActualizado) {
            return res.status(404).json({ error: 'Usuario no encontrado' });
        }

        res.status(200).json({ 
            message: 'Correo actualizado exitosamente', 
            usuario: usuarioActualizado 
        });

    } catch (error) {
        console.error('Error al cambiar el correo:', error);
        res.status(500).json({ error: 'Error interno al cambiar el correo' });
    }
}

export const cambiarContrasena = async (req, res) => {
    try {
        const { id } = req.params;
        const { contrasenaActual, nuevaContrasena } = req.body;

        if (!contrasenaActual || !nuevaContrasena) {
            return res.status(400).json({ error: 'La contraseña actual y la nueva son obligatorias' });
        }

        const usuario = await Usuario.findById(id);
        if (!usuario) {
            return res.status(404).json({ error: 'Usuario no encontrado' });
        }

        if (usuario.contrasena !== contrasenaActual) {
            return res.status(401).json({ error: 'La contraseña actual es incorrecta' });
        }

        usuario.contrasena = nuevaContrasena;
        await usuario.save();

        res.status(200).json({ message: 'Contraseña actualizada exitosamente' });

    } catch (error) {
        console.error('Error al cambiar la contraseña:', error);
        res.status(500).json({ error: 'Error interno al cambiar la contraseña' });
    }
}

export const subirFotoPerfil = async (req, res) => {
    try {
        const { id } = req.params;

        if (!req.file) {
            return res.status(400).json({ error: 'No se proporcionó ninguna imagen' });
        }

        const rutaImagen = `/uploads/${req.file.filename}`;

        const usuarioActualizado = await Usuario.findByIdAndUpdate(
            id, 
            { foto_perfil: rutaImagen }, 
            { new: true }
        );

        if (!usuarioActualizado) {
            return res.status(404).json({ error: 'Usuario no encontrado' });
        }

        res.status(200).json({ 
            message: 'Foto de perfil actualizada exitosamente', 
            usuario: usuarioActualizado 
        });

    } catch (error) {
        console.error('Error al subir la foto:', error);
        res.status(500).json({ error: 'Error interno al subir la foto' });
    }
}

export const eliminarCuenta = async (req, res) => {
    try {
        const { id } = req.params;
        const usuarioEliminado = await Usuario.findByIdAndDelete(id);

        if (!usuarioEliminado) {
            return res.status(404).json({ error: 'Usuario no encontrado' });
        }

        res.status(200).json({ message: 'Cuenta eliminada exitosamente' });

    } catch (error) {
        console.error('Error al eliminar la cuenta:', error);
        res.status(500).json({ error: 'Error interno al eliminar la cuenta' });
    }
}