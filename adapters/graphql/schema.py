'''
Archivo principal para definir el esquema de GraphQL
y conectar los resolvers y mutaciones.
'''
import graphene
from adapters.graphql.mutations import Mutation
from adapters.graphql.queries import Query


schema = graphene.Schema(query=Query, mutation=Mutation)
