"""
URL Configuration for bands
"""
from django.urls import path
from . import views   # import views from app
from . import classviews

app_name = 'bands'

urlpatterns = [
    # add url patterns for the bands app here

    # Example:
    path('', views.home, name='home'),
    path('sorted', views.bands_sorted, name='bandssorted'),
    path('list', views.bands_list, name='bandslist'),
    path('classlist', classviews.BandListView.as_view(), name='bandsclasslist'),
    path('class/<int:pk>', classviews.BandDetailView.as_view(), name='bandclassdetails'),
    path('listmore', views.bands_list_more, name='bandslistmore'),
    path('genre/<str:genre_name>', views.bands_by_genre, name='bandsbygenre'),
    path('search/<str:search_term>', views.bands_search, name='bandssearch'),
    path('<int:id>', views.band_details, name='banddetails'),
    path('<str:band_name>', views.band_basic, name='bandbasic'),
]
