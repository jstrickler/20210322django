"""
URL Configuration for dogs_core
"""
from django.urls import path
from . import views   # import views from app

app_name = "dogs_core"

urlpatterns = [
    # add url patterns for the dogs_core app here

    # Examples:
    # path('', views.home, name='home'),
    # path('thing', views.thing, name='thing'),
    path('', views.home, name='home'),
    path('details/<int:pkid>', views.dog_details, name='dog_details'),
    path('dogadd', views.dog_add, name='dog_add'),
    path('other', views.other_form, name='other')
]
