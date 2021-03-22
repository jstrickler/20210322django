"""
URL Configuration for presidents_core
"""
from django.urls import path, include

app_name = 'presidents_core'

urlpatterns = [
    # add url patterns for the presidents_core app here

    # Examples:
    # path('', views.home, name='home'),
    # path('thing', views.thing, name='thing'),
    path('api/', include('presidents_core.api.urls', namespace='api')),
]
