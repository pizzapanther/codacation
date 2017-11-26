from django.db.models import Q
from django.contrib.auth import get_user_model

import graphene
from graphene import relay
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from classroom.models import Klass

User = get_user_model()

class KlassNode (DjangoObjectType):
  is_admin = graphene.Boolean()
  
  class Meta:
    model = Klass
    filter_fields = ['id']
    interfaces = (relay.Node, )

  @classmethod
  def resolve_is_admin (cls, obj, info):
    return obj.is_admin(info.context.user)
    
  @classmethod
  def resolve_students (cls, obj, info):
    if obj.is_admin(info.context.user):
      return obj.students.all()
      
    return User.objects.none()
    
  @classmethod
  def resolve_admins (cls, obj, info):
    if obj.is_admin(info.context.user):
      return obj.admins.all()
      
    return User.objects.none()
    
class Query:
  my_classes = DjangoFilterConnectionField(KlassNode)
  
  def resolve_my_classes (self, info, **input):
    if info.context.user.is_authenticated():
      user = info.context.user
      return Klass.objects.filter(Q(admins=user) | Q(students=user))
      
    return Klass.objects.none()
    