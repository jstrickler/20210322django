"""
URL Configuration for demo
"""
from django.urls import path
from . import views   # import views from app

app_name = 'demo'

urlpatterns = [
    path('', views.home, name='home'),
    path('wombat', views.home, name='wombat'),
    path('ok/now/this/is/scary', views.home, name='scary'),
]
