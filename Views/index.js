import { connectDB } from '../config/db.js';
import { Genero } from '../Models/genero.js';
import { Usuario } from '../Models/usuarios.js';

const crearDatosIniciales = async () => {
  try {
    await connectDB();

    const nuevoGenero = await Genero.create({
      nombre: 'Rock'
    });
    console.log('Género creado:', nuevoGenero);

    const nuevoUsuario = await Usuario.create({
      nombre: 'Gael Gamez',
      apodo: 'gaelg',
      correo: 'gael@example.com',
      contrasena: '123456',
      genero: 'Masculino'
    });
    console.log('Usuario creado:', nuevoUsuario);

    console.log('Datos iniciales insertados correctamente.');
  } catch (error) {
    console.error('Error al insertar datos:', error.message);
  }
};

crearDatosIniciales();