"""
URL Configuration for core
"""
from django.urls import path
from . import views   # import views from app

urlpatterns = [
    # add url patterns for the core app here

    # Example:
   path('', views.home, name='home'),
]
