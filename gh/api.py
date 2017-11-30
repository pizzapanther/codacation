import requests

class RestAPI:
  def __init__ (self, user=None, token=None):
    self.token = token
    if token is None and user is not None:
      self.token = user.token
      
    self.url = 'https://api.github.com'
    
  def post (self, url, **kw):
    headers = {'Authorization': 'bearer ' + self.token}
    
    return requests.post(
      'https://api.github.com' + url, headers=headers, **kw)
    
  def get (self, url, **kw):
    headers = {'Authorization': 'bearer ' + self.token}
    
    return requests.get(
      'https://api.github.com' + url, headers=headers, **kw)
    
  def add_issue (self, owner, repo, **data):
    return self.post(f'/repos/{owner}/{repo}/issues', json=data)
    
  def create_branch (self, owner, repo, ref, sha):
    data = {
      'ref': ref,
      'sha': sha
    }
    return self.post(f'/repos/{owner}/{repo}/git/refs', json=data)
    
  def get_ref (self, owner, repo, ref):
    return self.get(f'/repos/{owner}/{repo}/git/refs/{ref}')
    