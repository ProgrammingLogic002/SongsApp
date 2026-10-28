from flask import Flask, request, jsonify
import graphene
from mongoengine import connect

# 1. Modelos (CRUD basico opcional si los quieres mantener expuestos)
from models import genero, usuario, cancion, lista_favoritos, favorito

# 2. Controladores (Logica avanzada)
from controllers import auth_controller, usuario_controller, cancion_controller, favorito_controller

# Conexion a Mongo
connect('songsapp_db', host='mongodb://admin:Z%258tKRvh%21UQA4okQ4gnGv%40@localhost:27017/')

# UNIFICACION DE QUERIES
class Query(
    genero.Query, 
    usuario.Query, 
    cancion.Query,
    lista_favoritos.Query,
    favorito.Query,
    auth_controller.Query,
    usuario_controller.Query,
    cancion_controller.Query,
    favorito_controller.Query,
    graphene.ObjectType
): pass

# UNIFICACION DE MUTATIONS
class Mutation(
    genero.Mutation, 
    usuario.Mutation, 
    cancion.Mutation, 
    lista_favoritos.Mutation,
    favorito.Mutation,
    auth_controller.Mutation,
    usuario_controller.Mutation,
    cancion_controller.Mutation,
    favorito_controller.Mutation,
    graphene.ObjectType
): pass

schema = graphene.Schema(query=Query, mutation=Mutation)
app = Flask(__name__)

@app.route('/graphql', methods=['POST'])
def graphql_api():
    data = request.get_json()
    result = schema.execute(data.get('query'))
    respuesta = {}
    if result.errors:
        respuesta['errors'] = [str(error) for error in result.errors]
    if result.data:
        respuesta['data'] = result.data
    return jsonify(respuesta)

if __name__ == '__main__':
    print("Servidor listo en: http://localhost:3000/graphql")
    app.run(port=3000)
