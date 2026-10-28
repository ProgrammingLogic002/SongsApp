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
    pass
class Mutation(graphene.ObjectType):
    pass
