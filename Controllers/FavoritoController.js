// 1. Mostrar los favoritos del usuario
export const obtenerFavoritos = async (req, res) => {
    try {
        res.status(200).json({ mensaje: "Lista de favoritos del usuario" });
    } catch (error) {
        res.status(500).json({ error: error.message });
    }
};

// 2. Agregar una canción
export const agregarAFavoritos = async (req, res) => {
    try {
        const { cancionId } = req.body;
        res.status(200).json({ mensaje: `Canción ${cancionId} agregada a favoritos` });
    } catch (error) {
        res.status(500).json({ error: error.message });
    }
};

// 3. Quitar una canción
export const quitarDeFavoritos = async (req, res) => {
    try {
        const { cancionId } = req.params;
        res.status(200).json({ mensaje: `Canción ${cancionId} eliminada de favoritos` });
    } catch (error) {
        res.status(500).json({ error: error.message });
    }
};

// 4. Cambiar el orden
export const cambiarOrdenFavoritos = async (req, res) => {
    try {
        const { nuevoOrden } = req.body;
        res.status(200).json({ mensaje: "Orden de favoritos actualizado" });
    } catch (error) {
        res.status(500).json({ error: error.message });
    }
};

// 5. Modificar la portada de la lista
export const modificarPortadaLista = async (req, res) => {
    try {
        const { rutaImagen } = req.body;
        res.status(200).json({ mensaje: "Portada de favoritos actualizada" });
    } catch (error) {
        res.status(500).json({ error: error.message });
    }
};

// 6. Reproducir las canciones en orden
export const reproducirEnOrden = async (req, res) => {
    try {
        res.status(200).json({ mensaje: "Reproduciendo favoritos en orden" });
    } catch (error) {
        res.status(500).json({ error: error.message });
    }
};