from django.db.models import Q

import graphene
from graphene import relay
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from classroom.models import Klass

class KlassNode (DjangoObjectType):
  is_admin = graphene.Boolean()
  
  class Meta:
    model = Klass
    filter_fields = ['id']
    interfaces = (relay.Node, )

  @classmethod
  def resolve_is_admin (cls, obj, info):
    if info.context.user.is_authenticated():
      if obj.admins.filter(id=info.context.user.id).count() > 0:
        return True
        
    return False
    
class Query:
  my_classes = DjangoFilterConnectionField(KlassNode)
  
  def resolve_my_classes (self, info, **input):
    if info.context.user.is_authenticated():
      user = info.context.user
      return Klass.objects.filter(Q(admins=user) | Q(students=user))
      
    return Klass.objects.none()
    