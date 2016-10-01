from django.conf.urls import url, include
from django.contrib import admin
import app_map.views

from .views import index

urlpatterns = [ url(r'^$',app_map.views.Home.as_view(),name='home'),
url(r'^project/', app_map.views.Project.as_view(), name='project'),
url(r'^help/',app_map.views.help, name='help'),
url(r'^req/',app_map.views.proseccing_request, name='req')



               ]

