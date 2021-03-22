"""
URL Configuration for api
"""
from django.urls import path
from . import views   # import views from app

app_name = 'api'

urlpatterns = [
    # add url patterns for the api app here

    # Example:
    # path('', views.home, name='home'),
    path('c2f/<celsius>/', views.CelsiusToFahrenheitView.as_view(), name='c2f'),
    path('f2c/<fahrenheit>/', views.FahrenheitToCelsiusView.as_view(), name='f2c'),
    path('c2f/', views.ErrorHandlerView.as_view(), name='invalid_c2f'),
    path('f2c/', views.ErrorHandlerView.as_view(), name='invalid_f2c'),
]
