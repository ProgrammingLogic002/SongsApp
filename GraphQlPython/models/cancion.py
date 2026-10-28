import graphene
from mongoengine import Document, StringField, ObjectIdField

class CancionModel(Document):
    meta = {'collection': 'Cancion'}
    nombre = StringField(required=True)
    autor = StringField()
    portada = StringField()
    archivo_audio = StringField()
    genero_id = ObjectIdField()

class CancionType(graphene.ObjectType):
    id = graphene.ID()
    nombre = graphene.String()
    autor = graphene.String()
    portada = graphene.String()
    archivo_audio = graphene.String()
    genero_id = graphene.ID()

class Query(graphene.ObjectType):
    obtener_canciones = graphene.List(CancionType)
    def resolve_obtener_canciones(self, info):
        return [CancionType(id=str(c.id), nombre=c.nombre, autor=c.autor, portada=c.portada, archivo_audio=c.archivo_audio, genero_id=str(c.genero_id)) for c in CancionModel.objects.all()]

class CrearCancion(graphene.Mutation):
    class Arguments:
        nombre = graphene.String(required=True)
        autor = graphene.String()
        portada = graphene.String()
        archivo_audio = graphene.String()
        genero_id = graphene.ID()
    cancion = graphene.Field(CancionType)
    def mutate(self, info, nombre, autor=None, portada=None, archivo_audio=None, genero_id=None):
        nuevo = CancionModel(nombre=nombre, autor=autor, portada=portada, archivo_audio=archivo_audio, genero_id=genero_id).save()
        return CrearCancion(cancion=CancionType(id=str(nuevo.id), nombre=nuevo.nombre, portada=nuevo.portada))

class Mutation(graphene.ObjectType):
    crear_cancion = CrearCancion.Field()
