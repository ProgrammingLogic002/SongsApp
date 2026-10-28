import graphene
from mongoengine import Document, IntField, ObjectIdField

class FavoritoModel(Document):
    meta = {'collection': 'Favorito'}
    lista_id = ObjectIdField(required=True)
    cancion_id = ObjectIdField(required=True)
    posicion = IntField(default=1)

class FavoritoType(graphene.ObjectType):
    id = graphene.ID()
    lista_id = graphene.ID()
    cancion_id = graphene.ID()
    posicion = graphene.Int()

class Query(graphene.ObjectType):
    obtener_favoritos = graphene.List(FavoritoType)
    
    def resolve_obtener_favoritos(self, info):
        return [
            FavoritoType(
                id=str(f.id), lista_id=str(f.lista_id), 
                cancion_id=str(f.cancion_id), posicion=f.posicion
            ) for f in FavoritoModel.objects.all()
        ]

class CrearFavorito(graphene.Mutation):
    class Arguments:
        lista_id = graphene.ID(required=True)
        cancion_id = graphene.ID(required=True)
        posicion = graphene.Int(default_value=1)
        
    favorito = graphene.Field(FavoritoType)
    
    def mutate(self, info, lista_id, cancion_id, posicion=1):
        nuevo = FavoritoModel(lista_id=lista_id, cancion_id=cancion_id, posicion=posicion)
        nuevo.save()
        return CrearFavorito(favorito=FavoritoType(
            id=str(nuevo.id), lista_id=str(nuevo.lista_id), 
            cancion_id=str(nuevo.cancion_id), posicion=nuevo.posicion
        ))

class ActualizarFavorito(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        lista_id = graphene.ID()
        cancion_id = graphene.ID()
        posicion = graphene.Int()
        
    favorito = graphene.Field(FavoritoType)
    
    def mutate(self, info, id, lista_id=None, cancion_id=None, posicion=None):
        favorito_obj = FavoritoModel.objects.get(id=id)
        if lista_id: favorito_obj.lista_id = lista_id
        if cancion_id: favorito_obj.cancion_id = cancion_id
        if posicion is not None: favorito_obj.posicion = posicion
        
        favorito_obj.save()
        return ActualizarFavorito(favorito=FavoritoType(
            id=str(favorito_obj.id), lista_id=str(favorito_obj.lista_id), 
            cancion_id=str(favorito_obj.cancion_id), posicion=favorito_obj.posicion
        ))

class EliminarFavorito(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
    
    success = graphene.Boolean()
    
    def mutate(self, info, id):
        favorito_obj = FavoritoModel.objects.get(id=id)
        favorito_obj.delete()
        return EliminarFavorito(success=True)

class Mutation(graphene.ObjectType):
    crear_favorito = CrearFavorito.Field()
    actualizar_favorito = ActualizarFavorito.Field()
    eliminar_favorito = EliminarFavorito.Field()
