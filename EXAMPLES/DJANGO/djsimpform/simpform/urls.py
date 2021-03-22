"""
URL Configuration for simpform
"""
from django.urls import path
from . import views   # import views from app

app_name = 'simpform'

urlpatterns = [
    # add url patterns for the simpform app here

    # Example:
    path('', views.home, name='home'),
]
