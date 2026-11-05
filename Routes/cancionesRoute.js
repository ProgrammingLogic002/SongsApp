import { Router } from 'express';
import {
    obtenerCancionesDisponibles,
    crearCancion,
    agruparPorGenero,
    obtenerDatosCancion,
    obtenerRutaAudio
} from '../Controllers/CancionController.js';

const router = Router();

// Rutas de catálogo de canciones
router.get('/', obtenerCancionesDisponibles);
router.post('/', crearCancion);
router.get('/genero', agruparPorGenero);
router.get('/:id', obtenerDatosCancion);
router.get('/:id/audio', obtenerRutaAudio);

export default router;