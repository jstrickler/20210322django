"""
URL Configuration for superheroes
"""
from django.urls import path
from . import views
from . import views_meta
from . import views_custom
from . import views_manager

app_name = 'superheroes'


urlpatterns = [
    path('', views.home, name='home'),
    path('herosort', views_meta.hero_sort, name='herosort'),
    path(
        'herodetails/<str:hero_name>)',
        views_meta.hero_details,
        name="herodetails",
    ),
    path(
        'flyerdetails/<str:hero_name>)',
        views_manager.hero_details,
        name="flyerdetails",
    ),
    path(
        'herocustom/<str:hero_name>)',
        views_custom.hero_custom,
        name="herocustom",
    ),
    path(
        'heromanager/',
        views_manager.hero_manager,
        name="heromanager",
    ),
]

