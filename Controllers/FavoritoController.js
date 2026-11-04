// FavoritoController.js

// 1. Mostrar los favoritos del usuario
const obtenerFavoritos = (req, res) => {
    res.json({ mensaje: "Lista de favoritos del usuario" });
};

// 2. Agregar una canción
const agregarAFavoritos = (req, res) => {
    const { cancionId } = req.body;
    res.json({ mensaje: `Canción ${cancionId} agregada a favoritos` });
};

// 3. Quitar una canción
const quitarDeFavoritos = (req, res) => {
    const { cancionId } = req.params;
    res.json({ mensaje: `Canción ${cancionId} eliminada de favoritos` });
};

// 4. Cambiar el orden
const cambiarOrdenFavoritos = (req, res) => {
    const { nuevoOrden } = req.body;
    res.json({ mensaje: "Orden de favoritos actualizado" });
};

// 5. Modificar la portada de la lista
const modificarPortadaLista = (req, res) => {
    const { rutaImagen } = req.body;
    res.json({ mensaje: "Portada de favoritos actualizada" });
};

// 6. Reproducir las canciones en orden
const reproducirEnOrden = (req, res) => {
    res.json({ mensaje: "Reproduciendo favoritos en orden" });
};

module.exports = {
    obtenerFavoritos,
    agregarAFavoritos,
    quitarDeFavoritos,
    cambiarOrdenFavoritos,
    modificarPortadaLista,
    reproducirEnOrden
};