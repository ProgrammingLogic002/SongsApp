import graphene
from mongoengine import Document, StringField, ObjectIdField

class ListaFavoritosModel(Document):
    meta = {'collection': 'ListaFavoritos'}
    usuario_id = ObjectIdField(required=True)
    portada = StringField()

class ListaFavoritosType(graphene.ObjectType):
    id = graphene.ID()
    usuario_id = graphene.ID()
    portada = graphene.String()

class Query(graphene.ObjectType):
    obtener_listas = graphene.List(ListaFavoritosType)
    
    def resolve_obtener_listas(self, info):
        return [
            ListaFavoritosType(
                id=str(l.id), usuario_id=str(l.usuario_id), portada=l.portada
            ) for l in ListaFavoritosModel.objects.all()
        ]

class CrearListaFavoritos(graphene.Mutation):
    class Arguments:
        usuario_id = graphene.ID(required=True)
        portada = graphene.String()
        
    lista = graphene.Field(ListaFavoritosType)
    
    def mutate(self, info, usuario_id, portada=None):
        nuevo = ListaFavoritosModel(usuario_id=usuario_id, portada=portada)
        nuevo.save()
        return CrearListaFavoritos(lista=ListaFavoritosType(
            id=str(nuevo.id), usuario_id=str(nuevo.usuario_id), portada=nuevo.portada
        ))

class ActualizarListaFavoritos(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        usuario_id = graphene.ID()
        portada = graphene.String()
        
    lista = graphene.Field(ListaFavoritosType)
    
    def mutate(self, info, id, usuario_id=None, portada=None):
        lista_obj = ListaFavoritosModel.objects.get(id=id)
        if usuario_id: lista_obj.usuario_id = usuario_id
        if portada: lista_obj.portada = portada
        
        lista_obj.save()
        return ActualizarListaFavoritos(lista=ListaFavoritosType(
            id=str(lista_obj.id), usuario_id=str(lista_obj.usuario_id), portada=lista_obj.portada
        ))

class EliminarListaFavoritos(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
    
    success = graphene.Boolean()
    
    def mutate(self, info, id):
        lista_obj = ListaFavoritosModel.objects.get(id=id)
        lista_obj.delete()
        return EliminarListaFavoritos(success=True)

class Mutation(graphene.ObjectType):
    crear_lista_favorita = CrearListaFavoritos.Field()
    actualizar_lista_favorita = ActualizarListaFavoritos.Field()
    eliminar_lista_favorita = EliminarListaFavoritos.Field()
