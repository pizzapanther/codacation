import logging
import random
from urllib.parse import urlparse

from django.contrib.auth import get_user_model
from django.utils.text import slugify

from gh.api import RestAPI
from classroom.models import Assignment, Issue

def create_issues(aid):
  ass = Assignment.objects.get(id=aid)
  
  logging.info(f'Creating Assignment: {ass.id} {ass.owner} {ass.repo_url}')
  
  url = urlparse(ass.repo_url)
  owner, repo = url.path[1:].split('/')
  
  github = RestAPI(user=ass.owner)
  response = github.get_ref(owner, repo, f'heads/master')
  sha = response.json()['object']['sha']
  
  for student in ass.klass.students.all():
    create_issue(
      ass.owner.token, ass.id, sha, ass.repo_url, ass.name, ass.short_description, student.id)
    
def create_issue (token, aid, sha, repo_url, title, desc, uid):
  student = get_user_model().objects.get(id=uid)
  social_auth = student.social_auth.get()
  ghuser = social_auth.extra_data['login']
  
  url = urlparse(repo_url)
  owner, repo = url.path[1:].split('/')
  logging.info(f'Issue -> {ghuser}, {owner}, {repo}')
  
  slug = slugify(title)
  r = random.randint(100, 1000)
  merge_branch = f'{ghuser}-{slug}-{r}'
  body = desc + "\n\n"
  body += f"@{ghuser} Merge onto branch: **{merge_branch}**\n\n"
  
  github = RestAPI(token=token)
  
  response = github.create_branch(
    owner, repo, f'refs/heads/{merge_branch}', sha)
  
  response = github.add_issue(
    owner, repo,
    title=f'{title} - {ghuser}',
    body=body,
  )
  
  issue_data = response.json()
  
  Issue.objects.create(
    num = issue_data['number'],
    merge_branch = merge_branch,
    assignment_id = aid,
    student = student
  )
  
  