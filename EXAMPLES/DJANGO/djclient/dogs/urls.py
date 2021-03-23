"""
URL Configuration for dogs
"""
from django.urls import path
from . import views   # import views from app

app_name = 'dogs'

urlpatterns = [
    # add url patterns for the dogs app here

    # Example:
   path('', views.home, name='home'),
]
