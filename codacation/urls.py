"""codacation URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from djzen.urls import zen_url

import codacation.views

urlpatterns = [
  zen_url('admin/', admin.site.urls),
  
  zen_url('auth/', include('social_django.urls', namespace='auth')),
  
  zen_url('gh/', include('gh.urls', namespace='gh')),
  
  zen_url('data-graph', codacation.views.data_graph),
  zen_url('favicon.ico', codacation.views.favicon),
  zen_url('.*', codacation.views.frontend),
]
