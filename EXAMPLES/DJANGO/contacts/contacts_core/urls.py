"""
URL Configuration for contacts_core
"""
from django.urls import path, include
from . import views   # import views from app

app_name = 'contacts_core'

urlpatterns = [
    path('api/', include('contacts_core.api.urls', namespace="api")),

]
