"""
URL Configuration for upload
"""
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from . import views   # import views from app

urlpatterns = [
    # add url patterns for the upload app here

    # Example:
    url(r'^$', views.home, name='home'),
    url(r'^simple_upload$', views.simple_upload, name='simple_upload'),
    url(r'^model_form_upload$', views.model_form_upload, name='model_form_upload'),
]


# needed to find /media/*
urlpatterns  += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
