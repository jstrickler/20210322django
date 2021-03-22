from django.urls import path, include
from . import viewsets  # import views from app
from rest_framework import routers

app_name = 'api'

router = routers.DefaultRouter()
router.register('presidents', viewsets.PresidentsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
