import { Cancion } from '../Models/cancion.js';

export const obtenerCancionesDisponibles = async (req, res) => {
    try {
        const canciones = await Cancion.find();
        res.status(200).json(canciones);
    } catch (error) {
        res.status(500).json({ mensaje: "Error al obtener las canciones", error: error.message });
    }
};

// 2. Crear una nueva canción
export const crearCancion = async (req, res) => {
    try {
        const { nombre, autor, portada, archivo_audio, genero } = req.body;
        
        const nuevaCancion = new Cancion({ 
            nombre, 
            autor, 
            portada, 
            archivo_audio, 
            genero 
        });

        await nuevaCancion.save();
        res.status(201).json({ mensaje: "Canción creada correctamente", cancion: nuevaCancion });
    } catch (error) {
        res.status(400).json({ mensaje: "Error al crear la canción", error: error.message });
    }
};

// 3. Agrupar por género
//falto reproducir lista de canciones 
export const agruparPorGenero = async (req, res) => {
    try {
        const cancionesPorGenero = await Cancion.aggregate([
            { $group: { _id: "$genero", canciones: { $push: "$$ROOT" } } }
        ]);
        res.status(200).json(cancionesPorGenero);
    } catch (error) {
        res.status(500).json({ mensaje: "Error al agrupar por género", error: error.message });
    }
};

// 4. Obtener datos por ID
export const obtenerDatosCancion = async (req, res) => {
    try {
        const { id } = req.params;
        const cancion = await Cancion.findById(id);
        if (!cancion) {
            return res.status(404).json({ mensaje: "Canción no encontrada" });
        }
        res.status(200).json(cancion);
    } catch (error) {
        res.status(500).json({ mensaje: "Error al buscar la canción", error: error.message });
    }
};

// 5. Ruta de audio
export const obtenerRutaAudio = async (req, res) => {
    try {
        const { id } = req.params;
        const cancion = await Cancion.findById(id).select('rutaAudio titulo');
        if (!cancion) {
            return res.status(404).json({ mensaje: "Canción no encontrada" });
        }
        res.status(200).json({ rutaAudio: cancion.rutaAudio });
    } catch (error) {
        res.status(500).json({ mensaje: "Error al obtener la ruta del audio", error: error.message });
    }
};

//falto crear lista