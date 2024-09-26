'''
Archivo principal para definir el esquema de GraphQL
y conectar los resolvers y mutaciones.
'''
import graphene

class Query(graphene.ObjectType):
    hello = graphene.String(default_value="Hola Mundo!")

schema = graphene.Schema(query=Query)
