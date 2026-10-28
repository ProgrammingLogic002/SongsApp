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
    pass
class Mutation(graphene.ObjectType):
    pass
