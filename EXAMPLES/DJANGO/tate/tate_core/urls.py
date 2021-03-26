"""
URL Configuration for tate_core
"""
from django.urls import path, include

app_name = 'tate_core'

urlpatterns = [
    # add url patterns for the tate_core app here

    # Examples:
    # path('', views.home, name='home'),
    # path('thing', views.thing, name='thing'),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
]
