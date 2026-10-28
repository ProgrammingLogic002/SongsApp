import graphene
from models.favorito import FavoritoModel, FavoritoType
from models.lista_favoritos import ListaFavoritosModel, ListaFavoritosType
from models.cancion import CancionModel

class CancionFavoritaDetalle(graphene.ObjectType):
    favorito_id = graphene.ID()
    cancion_id = graphene.ID()
    nombre = graphene.String()
    autor = graphene.String()
    posicion = graphene.Int()

class MisFavoritosType(graphene.ObjectType):
    lista_id = graphene.ID()
    portada = graphene.String()
    canciones = graphene.List(CancionFavoritaDetalle)

class Query(graphene.ObjectType):
    mis_favoritos = graphene.Field(MisFavoritosType, usuario_id=graphene.ID(required=True))
    reproducir_en_orden = graphene.List(graphene.String, lista_id=graphene.ID(required=True))

    def resolve_mis_favoritos(self, info, usuario_id):
        lista = ListaFavoritosModel.objects(usuario_id=usuario_id).first()
        if not lista: return None
        
        favoritos_bd = FavoritoModel.objects(lista_id=lista.id).order_by('posicion')
        canciones = []
        for fav in favoritos_bd:
            c = CancionModel.objects(id=fav.cancion_id).first()
            if c:
                canciones.append(CancionFavoritaDetalle(favorito_id=str(fav.id), cancion_id=str(c.id), nombre=c.nombre, autor=c.autor, posicion=fav.posicion))
                
        return MisFavoritosType(lista_id=str(lista.id), portada=lista.portada, canciones=canciones)

    def resolve_reproducir_en_orden(self, info, lista_id):
        favoritos_bd = FavoritoModel.objects(lista_id=lista_id).order_by('posicion')
        urls_audio = []
        for fav in favoritos_bd:
            c = CancionModel.objects(id=fav.cancion_id).first()
            if c and c.archivo_audio:
                urls_audio.append(c.archivo_audio)
        return urls_audio

class AgregarCancionFavorito(graphene.Mutation):
    class Arguments:
        lista_id = graphene.ID(required=True)
        cancion_id = graphene.ID(required=True)
    success = graphene.Boolean()
    def mutate(self, info, lista_id, cancion_id):
        total = FavoritoModel.objects(lista_id=lista_id).count()
        FavoritoModel(lista_id=lista_id, cancion_id=cancion_id, posicion=total+1).save()
        return AgregarCancionFavorito(success=True)

class QuitarCancionFavorito(graphene.Mutation):
    class Arguments:
        favorito_id = graphene.ID(required=True)
    success = graphene.Boolean()
    def mutate(self, info, favorito_id):
        FavoritoModel.objects(id=favorito_id).delete()
        return QuitarCancionFavorito(success=True)

class CambiarOrdenFavorito(graphene.Mutation):
    class Arguments:
        favorito_id = graphene.ID(required=True)
        nueva_posicion = graphene.Int(required=True)
    success = graphene.Boolean()
    def mutate(self, info, favorito_id, nueva_posicion):
        fav = FavoritoModel.objects.get(id=favorito_id)
        fav.posicion = nueva_posicion
        fav.save()
        return CambiarOrdenFavorito(success=True)

class ModificarPortadaLista(graphene.Mutation):
    class Arguments:
        lista_id = graphene.ID(required=True)
        nueva_portada = graphene.String(required=True)
    success = graphene.Boolean()
    def mutate(self, info, lista_id, nueva_portada):
        lista = ListaFavoritosModel.objects.get(id=lista_id)
        lista.portada = nueva_portada
        lista.save()
        return ModificarPortadaLista(success=True)

class Mutation(graphene.ObjectType):
    agregar_cancion_favorito = AgregarCancionFavorito.Field()
    quitar_cancion_favorito = QuitarCancionFavorito.Field()
    cambiar_orden_favorito = CambiarOrdenFavorito.Field()
    modificar_portada_lista = ModificarPortadaLista.Field()
