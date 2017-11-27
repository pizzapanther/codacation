from djzen.urls import zen_url

from gh.views import *

urlpatterns = [
  zen_url('repos', get_repos, name="repos")
]
