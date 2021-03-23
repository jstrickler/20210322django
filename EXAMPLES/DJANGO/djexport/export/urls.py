"""
URL Configuration for export
"""
from django.urls import path
from . import views   # import views from app

app_name = "export"

urlpatterns = [
    path('^$', views.home, name='home'),
    path('export_csv', views.export_csv, name='export_csv'),
    path('export_pdf', views.export_pdf, name='export_pdf'),
]
