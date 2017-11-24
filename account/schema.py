import datetime

from django.conf import settings

import graphene
from graphene import relay
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

import jwt

from account.models import User

def generate_jwt (user):
  exp = datetime.datetime.utcnow() + datetime.timedelta(days=14)
  
  encoded = jwt.encode(
    {
      'uid': user.id,
      'version': user.version,
      'email': user.email,
      'exp': exp
    },
    settings.SECRET_KEY,
    algorithm='HS256'
  )
  
  return encoded.decode('utf-8')

class GetJWT (relay.ClientIDMutation):
  class Input:
    extra = graphene.String(required=True)
    
  jwt = graphene.String()
  
  @classmethod
  def mutate_and_get_payload (cls, root, info, **input):
    if info.context.user.is_authenticated():
      return cls(jwt=generate_jwt(info.context.user))
      
    return cls(errors=['Not logged in'])
    
class AccountNode (DjangoObjectType):
  class Meta:
    model = User
    interfaces = (relay.Node, )
    filter_fields = []
    only_fields = ('email', 'first_name', 'last_name')
    
class Query:
  accounts = DjangoFilterConnectionField(AccountNode)
  
  def resolve_my_posts(self, info):
    if info.context.user.is_authenticated():
      return User.objects.filter(id=info.context.user.id)
      
    return User.objects.none()
    
class Mutation:
  get_jwt = GetJWT.Field()
  