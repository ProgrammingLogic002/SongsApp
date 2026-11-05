import { Router } from 'express';
import {
    obtenerFavoritos,
    agregarAFavoritos,
    quitarDeFavoritos,
    cambiarOrdenFavoritos,
    modificarPortadaLista,
    reproducirEnOrden
} from '../Controllers/FavoritoController.js';

const router = Router();

// Rutas de lista de favoritos
router.get('/', obtenerFavoritos);
router.post('/', agregarAFavoritos);
router.delete('/:cancionId', quitarDeFavoritos);
router.put('/orden', cambiarOrdenFavoritos);
router.put('/portada', modificarPortadaLista);
router.get('/reproducir', reproducirEnOrden);

export default router;