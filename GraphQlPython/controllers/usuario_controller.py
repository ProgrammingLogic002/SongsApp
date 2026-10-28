import graphene
import datetime
from models.usuario import UsuarioModel, UsuarioType

class MiPerfil(graphene.ObjectType):
    id = graphene.ID()
    nombre = graphene.String()
    apodo = graphene.String()
    correo = graphene.String()
    foto_perfil = graphene.String()

class Query(graphene.ObjectType):
    obtener_perfil = graphene.Field(MiPerfil, usuario_id=graphene.ID(required=True))
    
    def resolve_obtener_perfil(self, info, usuario_id):
        u = UsuarioModel.objects.get(id=usuario_id)
        return MiPerfil(id=str(u.id), nombre=u.nombre, apodo=u.apodo, correo=u.correo, foto_perfil=u.foto_perfil)

class ActualizarPerfil(graphene.Mutation):
    class Arguments:
        usuario_id = graphene.ID(required=True)
        nombre = graphene.String()
        apodo = graphene.String()
        correo = graphene.String()
        contrasena = graphene.String()
        foto_perfil = graphene.String()

    perfil = graphene.Field(MiPerfil)

    def mutate(self, info, usuario_id, nombre=None, apodo=None, correo=None, contrasena=None, foto_perfil=None):
        u = UsuarioModel.objects.get(id=usuario_id)
        if nombre: u.nombre = nombre
        if apodo: u.apodo = apodo
        if correo: u.correo = correo
        if contrasena: u.contrasena = contrasena
        if foto_perfil: u.foto_perfil = foto_perfil
        u.updatedAt = datetime.datetime.utcnow()
        u.save()
        return ActualizarPerfil(perfil=MiPerfil(id=str(u.id), nombre=u.nombre, apodo=u.apodo, correo=u.correo, foto_perfil=u.foto_perfil))

class EliminarCuenta(graphene.Mutation):
    class Arguments:
        usuario_id = graphene.ID(required=True)
    success = graphene.Boolean()

    def mutate(self, info, usuario_id):
        UsuarioModel.objects(id=usuario_id).delete()
        # Aqui podriamos borrar tambien sus favoritos, etc.
        return EliminarCuenta(success=True)

class Mutation(graphene.ObjectType):
    actualizar_perfil = ActualizarPerfil.Field()
    eliminar_cuenta = EliminarCuenta.Field()
