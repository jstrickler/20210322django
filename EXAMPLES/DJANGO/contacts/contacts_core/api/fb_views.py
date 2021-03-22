# not needed for REST CBVs or Viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from contacts_core.models import Contact
from .serializers import ContactSerializerPlain

# Create your RESTful views here.

# example without template (only used in class -- always use templates in real life):
@api_view(['GET'])
def hello(request):
     message = {"message": "Welcome to Contacts API Core"}
     renderer = JSONRenderer()
     return Response(renderer.render(message), 200)

@api_view(['GET'])
def contacts(request):
     contacts = Contact.objects.all()
     serializer = ContactSerializerPlain(contacts, many=True)
     contacts_json = JSONRenderer().render(serializer.data)
     return Response(contacts_json, 200)

@api_view(['GET'])
def contacts_detail(request, pk):
     contacts = Contact.objects.filter(id=pk)
     serializer = ContactSerializerPlain(contacts)
     contacts_json = JSONRenderer().render(serializer.data)
     return Response(contacts_json, 200)

