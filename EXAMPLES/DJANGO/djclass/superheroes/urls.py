"""
URL Configuration for superheroes
"""
from django.conf.urls import url
from django.urls import path
from django.views.generic import TemplateView
from . import views

app_name = 'superheroes'

urlpatterns = [
    # welcome page, no class-based views
    path(
        '',
        views.HomeView.as_view,
        name = 'home'
    ),

    # NO view -- don't do this:
    path(
        'noview',
        TemplateView.as_view(template_name='noview.html'),
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
        'genericcontext',
        views.GenericContext.as_view(),
        name="genericcontext",
    ),
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
    path(
        'heroupdate/<int:pk>',
        views.HeroUpdateView.as_view(),
        name="heroupdate",
    ),
    path(
        'success', views.SuccessView.as_view(), name="success",
    )
]

