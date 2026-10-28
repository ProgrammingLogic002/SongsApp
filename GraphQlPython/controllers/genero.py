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
        return [
            GeneroType(
                id=str(g.id), nombre=g.nombre, 
                createdAt=g.createdAt, updatedAt=g.updatedAt, version=g.version
            ) for g in GeneroModel.objects.all()
        ]

class CrearGenero(graphene.Mutation):
    class Arguments:
        nombre = graphene.String(required=True)
    
    genero = graphene.Field(GeneroType)
    
    def mutate(self, info, nombre):
        ahora = datetime.datetime.utcnow()
        nuevo = GeneroModel(nombre=nombre, createdAt=ahora, updatedAt=ahora, version=0)
        nuevo.save()
        return CrearGenero(genero=GeneroType(id=str(nuevo.id), nombre=nuevo.nombre, createdAt=nuevo.createdAt, updatedAt=nuevo.updatedAt, version=nuevo.version))

class ActualizarGenero(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        nombre = graphene.String()

    genero = graphene.Field(GeneroType)

    def mutate(self, info, id, nombre=None):
        genero_obj = GeneroModel.objects.get(id=id)
        if nombre:
            genero_obj.nombre = nombre
        genero_obj.updatedAt = datetime.datetime.utcnow()
        genero_obj.save()
        return ActualizarGenero(genero=GeneroType(id=str(genero_obj.id), nombre=genero_obj.nombre, createdAt=genero_obj.createdAt, updatedAt=genero_obj.updatedAt, version=genero_obj.version))

class EliminarGenero(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    success = graphene.Boolean()

    def mutate(self, info, id):
        genero_obj = GeneroModel.objects.get(id=id)
        genero_obj.delete()
        return EliminarGenero(success=True)

class Mutation(graphene.ObjectType):
    crear_genero = CrearGenero.Field()
    actualizar_genero = ActualizarGenero.Field()
    eliminar_genero = EliminarGenero.Field()
