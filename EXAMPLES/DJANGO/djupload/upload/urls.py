"""
URL Configuration for upload
"""
from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from . import views   # import views from app

app_name = 'superheroes'

urlpatterns = [
    # add url patterns for the upload app here

    # Example:
    path('', views.home, name='home'),
    path('simple_upload', views.simple_upload, name='simple_upload'),
    path('model_form_upload', views.model_form_upload, name='model_form_upload'),
]


# needed to find /media/*
urlpatterns  += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
