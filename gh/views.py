from string import Template

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

import requests

GH_ENDPOINT = 'https://api.github.com/graphql'

def get_all_repos(token, repos=None, after=None):
  if repos is None:
    repos = []
    
  a = ''
  if after:
    a = 'after: "{}"'.format(after)
  q = """query {
    viewer { 
      repositories(first: 100 $after orderBy: {field: PUSHED_AT, direction: DESC}) {
        edges{
          node{
            id
            name
            url
            isPrivate
            pushedAt
          }
        }
        pageInfo{
          startCursor
          hasNextPage
          endCursor
        }
      }
    }
  }"""
  
  q = Template(q)
  q = q.substitute(after=a)
  
  headers = {'Authorization': 'bearer ' + token}
  response = requests.post(GH_ENDPOINT, json={'query': q}, headers=headers)
  data = response.json()['data']['viewer']['repositories']
  
  for edge in data['edges']:
    repos.append(edge['node'])
    
  if data['pageInfo']['hasNextPage']:
    get_all_repos(token, repos, data['pageInfo']['endCursor'])
    
  return repos
  
@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def get_repos (request):
  auth = request.user.social_auth.get()
  return Response(get_all_repos(auth.access_token))
  