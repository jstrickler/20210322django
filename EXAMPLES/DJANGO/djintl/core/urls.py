"""
URL Configuration for core
"""
from django.conf.urls import url
from . import views   # import views from app

urlpatterns = [
    # add url patterns for the core app here

    # Example:
   url(r'^$', views.home, name='home'),
]
