from rest_framework import viewsets
from contacts_core.api.serializers import ContactSerializer, CitySerializer
#  from contacts_core.api.filters import * # (optional)  change to only needed serializers
from contacts_core.models import Contact, City

class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    # filter_backends = [DjangoFilterBackend]
    # filterset_class = MyFirstModelFilter
    # pagination_class = ...


class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    # filter_backends = [DjangoFilterBackend]
    # filterset_class = MySecondModelFilter

