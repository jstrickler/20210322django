"""
URL Configuration for dogs_core
"""
from django.urls import path, include

app_name = 'dogs_core'

urlpatterns = [
    # add url patterns for the dogs_core app here

    # Examples:
    # path('', views.home, name='home'),
    # path('thing', views.thing, name='thing'),
    path('api/', include('dogs_core.api.urls', namespace="api")),  # delegate to app's URL config

]
