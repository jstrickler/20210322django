"""
URL Configuration for superheroes
"""
from django.urls import path
from . import views   # import views from app
from . import views404
from . import viewsbasictemplate
from . import viewstemplate
from . import viewsqueries

app_name = 'superheroes'

urlpatterns = [
    path('', views.home, name='home'),  # 'superheroes:home'
                                        # 'NAMESPACE:VIEW'
    path('hero/<str:hero_name>/', views.hero, name="hero"),


    path('hero404x/<str:hero_name>/', views404.hero404, name="hero404"),
    path('hero404sc/<str:hero_name>/', views404.hero404sc, name="hero404sc"),
    path(
        'herotemplate101/<str:hero_name>/',
        viewsbasictemplate.hero_basic_template,
        name="herobasictemplate",
    ),
    path(
        'herohardway/<str:hero_name>/',
        viewstemplate.hero_hard_way,
        name="herohardway",
    ),
    path(
        'heroeasyway/<str:hero_name>/',
        viewstemplate.hero_easy_way,
        name="heroeasyway",
    ),
    path(
        'herolookups/<str:hero_name>/',
        viewstemplate.hero_lookups,
        name="herolookups",
    ),
    path(
        'herofilters/<str:hero_name>/',
        viewstemplate.hero_filters,
        name="herofilters",
    ),
    path(
        'herotags/<str:hero_name>/',
        viewstemplate.hero_tags,
        name="herotags",
    ),
    path(
        'herodetails/<str:hero_name>/',
        viewstemplate.hero_details,
        name="herodetails",
    ),
    path(
        'heroescape/<str:hero_name>/',
        viewstemplate.hero_escape,
        name="heroescape",
    ),
    path(
        'herourls/',
        viewstemplate.hero_urls,
        name="herourls",
    ),
    path(
        'herostatic/<str:hero_name>/',
        viewstemplate.hero_static,
        name="herostatic",
    ),
    path(
        'heroqueries/',
        viewsqueries.hero_queries,
        name="heroqueries",
    ),
    path(
        'session1', views.session1, name='session1'
    ),
    path(
        'session2', views.session2, name='session2'
    ),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]

