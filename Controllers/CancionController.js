// 1. Mostrar las canciones disponibles
const obtenerCancionesDisponibles = (req, res) => {
    res.json({ mensaje: "Lista de canciones disponibles" });
};

// 2. Agruparlas por género
const agruparPorGenero = (req, res) => {
    res.json({ mensaje: "Canciones agrupadas por género" });
};

// 3. Obtener los datos de una canción
const obtenerDatosCancion = (req, res) => {
    const { id } = req.params;
    res.json({ mensaje: `Datos de la canción ${id}` });
};

// 4. Entregar la dirección del archivo de audio
const obtenerRutaAudio = (req, res) => {
    const { id } = req.params;
    res.json({ ruta: `/audio/cancion_${id}.mp3` });
};

module.exports = {
    obtenerCancionesDisponibles,
    agruparPorGenero,
    obtenerDatosCancion,
    obtenerRutaAudio
};