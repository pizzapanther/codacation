import graphene

import account.schema
import classroom.schema

class Query(
  account.schema.Query,
  classroom.schema.Query,
  graphene.ObjectType):
  pass

class Mutation(
  account.schema.Mutation,
  graphene.ObjectType):
  pass

schema = graphene.Schema(query=Query, mutation=Mutation)
