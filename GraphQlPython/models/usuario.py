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
    foto_perfil = StringField() # Nuevo campo
    token = StringField()       # Nuevo campo para sesiones
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
    foto_perfil = graphene.String()
    token = graphene.String()
    createdAt = graphene.DateTime()
    updatedAt = graphene.DateTime()

class Query(graphene.ObjectType):
    obtener_usuarios = graphene.List(UsuarioType)
    def resolve_obtener_usuarios(self, info):
        return [UsuarioType(id=str(u.id), nombre=u.nombre, apodo=u.apodo, correo=u.correo, foto_perfil=u.foto_perfil) for u in UsuarioModel.objects.all()]

class Mutation(graphene.ObjectType):
    pass
