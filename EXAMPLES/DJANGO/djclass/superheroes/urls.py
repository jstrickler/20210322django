"""
URL Configuration for superheroes
"""
from django.conf.urls import url
from django.urls import path
from django.views.generic import TemplateView  # BAD PRACTICE
from . import views

app_name = 'superheroes'

urlpatterns = [
    # welcome page, no class-based views
    path('wombat', views.WombatView.as_view(), name="wombat"),
    path(
        '',
        views.HomeView.as_view(),
        name = 'home'
    ),

    # NO view -- don't do this:
    path(
        'noview',
        TemplateView.as_view(template_name='superheroes/noview.html'),
        name="noview",
    ),

    # minimal views with models
    path(
        'minimallist',
        views.HeroListViewMinimal.as_view(),
        name="minimallist",
    ),
    path(
        'minimaldetails/<int:pk>',
        views.HeroDetailViewMinimal.as_view(),
        name="minimaldetails",
    ),

    #

    path(
        'genericlist',
        views.HeroListView.as_view(),
        name="genericlist",
    ),
    path(
        'genericdetail/<int:pk>',
        views.HeroDetailView.as_view(),
        name="genericdetail",
    ),
    path(
        'herocreate',
        views.HeroCreateView.as_view(),
        name="herocreate",
    ),
    path('citycreate', views.CityCreateView.as_view(), name='citycreate'),
    path(
        'heroupdate/<int:pk>',
        views.HeroUpdateView.as_view(),
        name="heroupdate",
    ),
    path(
        'success', views.SuccessView.as_view(), name="success",
    )
]

