from django.urls import path, include
from rest_framework import routers

from . import fb_views
from . import cb_views
from . import viewsets

app_name = 'api'

router = routers.DefaultRouter()
router.register('contacts', viewsets.ContactViewSet)
router.register('cities', viewsets.CityViewSet)

urlpatterns = [
    # path('fbv/hello', fb_views.hello, name="hello"),
    path('fbv/hello', fb_views.hello, name="hello"),
    path('fbv/contacts', fb_views.contacts, name="fbcontacts"),
    path('fbv/contacts/<str:pk>', fb_views.contacts_detail, name="fbcontacts-detail"),
    path('cbv/contacts', cb_views.ContactsList.as_view(), name="contacts"),
    path('cbv/contacts/<str:pk>', cb_views.ContactsDetail.as_view(), name="cbcontacts-detail"),
#    path('cbv/contactsx/<str:pk>', cb_views.ContactsList.as_view(), name="cbcontacts-detail"),
    path('cbv/cities', cb_views.CitiesList.as_view(), name="cities"),
    path('cbv/cities/<str:pk>', cb_views.CitiesDetail.as_view(), name="cbcities-detail"),
    path('', include(router.urls)),
]

