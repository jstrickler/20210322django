"""
URL Configuration for dogs
"""
from django.conf.urls import url
from . import views   # import views from app

urlpatterns = [
    # add url patterns for the dogs app here

    # Example:
   url(r'^$', views.home, name='home'),
]
