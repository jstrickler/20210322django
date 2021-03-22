# not needed for REST CBVs or Viewsets
from contacts_core.models import Contact, City
from rest_framework import generics
from  .serializers import ContactSerializer, CitySerializer

# class-based views (aka CBVs)
class ContactsList(generics.ListCreateAPIView):   #  GET /api/contacts  POST /api/contacts

    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

class ContactsDetail(generics.RetrieveUpdateDestroyAPIView):
    # GET /api/contacts/ID  PUT /api/contacts/ID  PATCH /api/contacts/ID  DELETE /api/contacts/ID
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

class CitiesList(generics.ListCreateAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer

class CitiesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer
