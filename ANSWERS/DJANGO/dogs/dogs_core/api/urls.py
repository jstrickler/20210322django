from django.urls import path, include
from rest_framework import routers
from . import views
from . import viewsets

app_name = 'api'

router = routers.DefaultRouter()
router.register(r'dogs', viewsets.DogsViewSet)
router.register(r'breeds', viewsets.BreedsViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('fbv/dogs', views.dogs, name="fbdogs"),
    path('cbv/dogs', views.DogsList.as_view(), name="dogs-cbv"),
    path('cbv/dogs/<str:pk>', views.DogsDetail.as_view(), name="dogs-detail-cbv"),
    path('cbv/breeds', views.BreedsList.as_view(), name="breeds-cbv"),
    path('cbv/breeds/<str:pk>', views.BreedsDetail.as_view(), name="breeds-detail-cbv"),
]







