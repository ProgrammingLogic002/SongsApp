import graphene
import uuid
import datetime
from models.usuario import UsuarioModel, UsuarioType
from models.lista_favoritos import ListaFavoritosModel

class RegistrarUsuario(graphene.Mutation):
    class Arguments:
        nombre = graphene.String(required=True)
        correo = graphene.String(required=True)
        contrasena = graphene.String(required=True)
        confirmar_contrasena = graphene.String(required=True)

    usuario = graphene.Field(UsuarioType)
    mensaje = graphene.String()

    def mutate(self, info, nombre, correo, contrasena, confirmar_contrasena):
        if contrasena != confirmar_contrasena:
            raise Exception("Las contrasenas no coinciden")
        if UsuarioModel.objects(correo=correo).first():
            raise Exception("El correo ya esta en uso")
            
        token_acceso = str(uuid.uuid4())
        nuevo_usuario = UsuarioModel(
            nombre=nombre, correo=correo, contrasena=contrasena, token=token_acceso
        )
        nuevo_usuario.save()

        # Crear lista de favoritos por defecto
        ListaFavoritosModel(usuario_id=nuevo_usuario.id, portada="default.png").save()

        return RegistrarUsuario(
            usuario=UsuarioType(id=str(nuevo_usuario.id), nombre=nuevo_usuario.nombre, token=nuevo_usuario.token),
            mensaje="Usuario registrado e iniciada la sesion correctamente"
        )

class IniciarSesion(graphene.Mutation):
    class Arguments:
        correo = graphene.String(required=True)
        contrasena = graphene.String(required=True)

    usuario = graphene.Field(UsuarioType)
    mensaje = graphene.String()

    def mutate(self, info, correo, contrasena):
        usuario = UsuarioModel.objects(correo=correo, contrasena=contrasena).first()
        if not usuario:
            raise Exception("Correo o contrasena incorrectos")
            
        usuario.token = str(uuid.uuid4())
        usuario.save()
        return IniciarSesion(usuario=UsuarioType(id=str(usuario.id), nombre=usuario.nombre, token=usuario.token), mensaje="Sesion iniciada")

class CerrarSesion(graphene.Mutation):
    class Arguments:
        usuario_id = graphene.ID(required=True)

    mensaje = graphene.String()

    def mutate(self, info, usuario_id):
        usuario = UsuarioModel.objects(id=usuario_id).first()
        if usuario:
            usuario.token = ""
            usuario.save()
        return CerrarSesion(mensaje="Sesion cerrada exitosamente")

class Mutation(graphene.ObjectType):
    registrar_usuario = RegistrarUsuario.Field()
    iniciar_sesion = IniciarSesion.Field()
    cerrar_sesion = CerrarSesion.Field()
class Query(graphene.ObjectType):
    pass
