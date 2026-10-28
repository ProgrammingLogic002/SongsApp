import graphene
from mongoengine import Document, StringField, DateTimeField, IntField
import datetime

class UsuarioModel(Document):
    meta = {'collection': 'Usuario'}
    nombre = StringField(required=True)
    apodo = StringField()
    correo = StringField()
    contrasena = StringField()
    genero = StringField()
    createdAt = DateTimeField(default=datetime.datetime.utcnow)
    updatedAt = DateTimeField(default=datetime.datetime.utcnow)
    version = IntField(db_field='__v', default=0)

class UsuarioType(graphene.ObjectType):
    id = graphene.ID()
    nombre = graphene.String()
    apodo = graphene.String()
    correo = graphene.String()
    contrasena = graphene.String()
    genero = graphene.String()
    createdAt = graphene.DateTime()
    updatedAt = graphene.DateTime()

class Query(graphene.ObjectType):
    obtener_usuarios = graphene.List(UsuarioType)
    
    def resolve_obtener_usuarios(self, info):
        return [
            UsuarioType(
                id=str(u.id), nombre=u.nombre, apodo=u.apodo, 
                correo=u.correo, contrasena=u.contrasena, genero=u.genero, 
                createdAt=u.createdAt, updatedAt=u.updatedAt
            ) for u in UsuarioModel.objects.all()
        ]

class CrearUsuario(graphene.Mutation):
    class Arguments:
        nombre = graphene.String(required=True)
        apodo = graphene.String()
        correo = graphene.String()
        contrasena = graphene.String()
        genero = graphene.String()
        
    usuario = graphene.Field(UsuarioType)
    
    def mutate(self, info, nombre, apodo=None, correo=None, contrasena=None, genero=None):
        ahora = datetime.datetime.utcnow()
        nuevo = UsuarioModel(
            nombre=nombre, apodo=apodo, correo=correo, 
            contrasena=contrasena, genero=genero,
            createdAt=ahora, updatedAt=ahora, version=0
        )
        nuevo.save()
        return CrearUsuario(usuario=UsuarioType(id=str(nuevo.id), nombre=nuevo.nombre, apodo=nuevo.apodo, correo=nuevo.correo, contrasena=nuevo.contrasena, genero=nuevo.genero, createdAt=nuevo.createdAt, updatedAt=nuevo.updatedAt))

class ActualizarUsuario(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        nombre = graphene.String()
        apodo = graphene.String()
        correo = graphene.String()
        contrasena = graphene.String()
        genero = graphene.String()

    usuario = graphene.Field(UsuarioType)

    def mutate(self, info, id, nombre=None, apodo=None, correo=None, contrasena=None, genero=None):
        usuario_obj = UsuarioModel.objects.get(id=id)
        if nombre: usuario_obj.nombre = nombre
        if apodo: usuario_obj.apodo = apodo
        if correo: usuario_obj.correo = correo
        if contrasena: usuario_obj.contrasena = contrasena
        if genero: usuario_obj.genero = genero
        
        usuario_obj.updatedAt = datetime.datetime.utcnow()
        usuario_obj.save()
        return ActualizarUsuario(usuario=UsuarioType(id=str(usuario_obj.id), nombre=usuario_obj.nombre, apodo=usuario_obj.apodo, correo=usuario_obj.correo, contrasena=usuario_obj.contrasena, genero=usuario_obj.genero, createdAt=usuario_obj.createdAt, updatedAt=usuario_obj.updatedAt))

class EliminarUsuario(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
    
    success = graphene.Boolean()

    def mutate(self, info, id):
        usuario_obj = UsuarioModel.objects.get(id=id)
        usuario_obj.delete()
        return EliminarUsuario(success=True)

class Mutation(graphene.ObjectType):
    crear_usuario = CrearUsuario.Field()
    actualizar_usuario = ActualizarUsuario.Field()
    eliminar_usuario = EliminarUsuario.Field()
