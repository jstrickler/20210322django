"""
URL Configuration for export
"""
from django.conf.urls import url
from . import views   # import views from app

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^export_csv$', views.export_csv, name='export_csv'),
    url(r'^export_pdf$', views.export_pdf, name='export_pdf'),
]
