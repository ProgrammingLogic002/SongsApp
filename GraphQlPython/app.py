from flask import Flask, request, jsonify
import graphene
from mongoengine import connect

# 1. Importamos las clases Query y Mutation de cada controlador
from controllers import genero, usuario, cancion, lista_favoritos, favorito

# 2. Conexion a Mongo
connect('songsapp_db', host='mongodb://admin:Z%258tKRvh%21UQA4okQ4gnGv%40@localhost:27017/')

# 3. UNIFICACION DE QUERIES (Herencia Multiple)
class Query(
    genero.Query, 
    usuario.Query, 
    cancion.Query,
    lista_favoritos.Query,
    favorito.Query,
    graphene.ObjectType
):
    pass

# 4. UNIFICACION DE MUTATIONS
class Mutation(
    genero.Mutation, 
    usuario.Mutation, 
    cancion.Mutation, 
    lista_favoritos.Mutation,
    favorito.Mutation,
    graphene.ObjectType
):
    pass

# 5. Compilacion del esquema final
schema = graphene.Schema(query=Query, mutation=Mutation)

app = Flask(__name__)

@app.route('/graphql', methods=['POST'])
def graphql_api():
    data = request.get_json()
    query = data.get('query')
    
    result = schema.execute(query)
    
    respuesta = {}
    if result.errors:
        respuesta['errors'] = [str(error) for error in result.errors]
    if result.data:
        respuesta['data'] = result.data
    
    return jsonify(respuesta)

if __name__ == '__main__':
    print("🚀 Servidor listo en: http://localhost:3000/graphql")
    app.run(port=3000)
