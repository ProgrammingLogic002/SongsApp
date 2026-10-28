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
        return [
            CancionType(
                id=str(c.id), nombre=c.nombre, autor=c.autor,
                portada=c.portada, archivo_audio=c.archivo_audio,
                genero_id=str(c.genero_id)
            ) for c in CancionModel.objects.all()
        ]

class CrearCancion(graphene.Mutation):
    class Arguments:
        nombre = graphene.String(required=True)
        autor = graphene.String()
        portada = graphene.String()
        archivo_audio = graphene.String()
        genero_id = graphene.ID()
        
    cancion = graphene.Field(CancionType)
    
    def mutate(self, info, nombre, autor=None, portada=None, archivo_audio=None, genero_id=None):
        nuevo = CancionModel(nombre=nombre, autor=autor, portada=portada, archivo_audio=archivo_audio, genero_id=genero_id)
        nuevo.save()
        return CrearCancion(cancion=CancionType(
            id=str(nuevo.id), nombre=nuevo.nombre, autor=nuevo.autor, 
            portada=nuevo.portada, archivo_audio=nuevo.archivo_audio, genero_id=str(nuevo.genero_id)
        ))

class ActualizarCancion(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        nombre = graphene.String()
        autor = graphene.String()
        portada = graphene.String()
        archivo_audio = graphene.String()
        genero_id = graphene.ID()
        
    cancion = graphene.Field(CancionType)
    
    def mutate(self, info, id, nombre=None, autor=None, portada=None, archivo_audio=None, genero_id=None):
        cancion_obj = CancionModel.objects.get(id=id)
        if nombre: cancion_obj.nombre = nombre
        if autor: cancion_obj.autor = autor
        if portada: cancion_obj.portada = portada
        if archivo_audio: cancion_obj.archivo_audio = archivo_audio
        if genero_id: cancion_obj.genero_id = genero_id
        
        cancion_obj.save()
        return ActualizarCancion(cancion=CancionType(
            id=str(cancion_obj.id), nombre=cancion_obj.nombre, autor=cancion_obj.autor, 
            portada=cancion_obj.portada, archivo_audio=cancion_obj.archivo_audio, genero_id=str(cancion_obj.genero_id)
        ))

class EliminarCancion(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
    
    success = graphene.Boolean()

    def mutate(self, info, id):
        cancion_obj = CancionModel.objects.get(id=id)
        cancion_obj.delete()
        return EliminarCancion(success=True)

class Mutation(graphene.ObjectType):
    crear_cancion = CrearCancion.Field()
    actualizar_cancion = ActualizarCancion.Field()
    eliminar_cancion = EliminarCancion.Field()
