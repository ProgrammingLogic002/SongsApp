import graphene
from models.cancion import CancionModel, CancionType
from models.genero import GeneroModel

class CancionesPorGenero(graphene.ObjectType):
    genero_nombre = graphene.String()
    canciones = graphene.List(CancionType)

class Query(graphene.ObjectType):
    canciones_agrupadas = graphene.List(CancionesPorGenero)
    datos_cancion = graphene.Field(CancionType, cancion_id=graphene.ID(required=True))
    audio_cancion = graphene.String(cancion_id=graphene.ID(required=True))

    def resolve_canciones_agrupadas(self, info):
        resultado = []
        generos = GeneroModel.objects.all()
        for g in generos:
            canciones_bd = CancionModel.objects(genero_id=g.id)
            lista_canciones = [CancionType(id=str(c.id), nombre=c.nombre, autor=c.autor, archivo_audio=c.archivo_audio) for c in canciones_bd]
            if lista_canciones:
                resultado.append(CancionesPorGenero(genero_nombre=g.nombre, canciones=lista_canciones))
        return resultado

    def resolve_datos_cancion(self, info, cancion_id):
        c = CancionModel.objects.get(id=cancion_id)
        return CancionType(id=str(c.id), nombre=c.nombre, autor=c.autor, portada=c.portada)

    def resolve_audio_cancion(self, info, cancion_id):
        c = CancionModel.objects.get(id=cancion_id)
        return c.archivo_audio

class Mutation(graphene.ObjectType):
    pass
