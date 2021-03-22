"""
URL Configuration for fleek
"""
from django.urls import path
from . import views   # import views from app

app_name = 'fleek'

urlpatterns = [
    # add url patterns for the fleek app here

    # Examples:
    # path('', views.home, name='home'),
    path('', views.home, name='home'),
    path('vogg', views.vogg, name='vogg'),
    path('blenn', views.blenn, name='blenn'),
]
