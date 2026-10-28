import graphene
from mongoengine import Document, StringField, DateTimeField, IntField
import datetime

class GeneroModel(Document):
    meta = {'collection': 'Genero'}
    nombre = StringField(required=True)
    createdAt = DateTimeField(default=datetime.datetime.utcnow)
    updatedAt = DateTimeField(default=datetime.datetime.utcnow)
    version = IntField(db_field='__v', default=0)

class GeneroType(graphene.ObjectType):
    id = graphene.ID()
    nombre = graphene.String()
    createdAt = graphene.DateTime()
    updatedAt = graphene.DateTime()
    version = graphene.Int()
    
class Query(graphene.ObjectType):
    obtener_generos = graphene.List(GeneroType)
    def resolve_obtener_generos(self, info):
        return [GeneroType(id=str(g.id), nombre=g.nombre, createdAt=g.createdAt, updatedAt=g.updatedAt) for g in GeneroModel.objects.all()]

class CrearGenero(graphene.Mutation):
    class Arguments: nombre = graphene.String(required=True)
    genero = graphene.Field(GeneroType)
    def mutate(self, info, nombre):
        nuevo = GeneroModel(nombre=nombre).save()
        return CrearGenero(genero=GeneroType(id=str(nuevo.id), nombre=nuevo.nombre))

class Mutation(graphene.ObjectType):
    crear_genero = CrearGenero.Field()
