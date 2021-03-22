from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from dogs_core.models import Dog, Breed
from rest_framework import generics
from  .serializers import DogSerializerX, DogSerializer, BreedSerializer

@api_view(['GET'])
def dogs(request):
     dogs = Dog.objects.all()
     serializer = DogSerializerX(dogs, many=True)
     dogs_json = JSONRenderer().render(serializer.data)
     return Response(dogs_json, 200)


# class-based views (aka CBVs)
class DogsList(generics.ListCreateAPIView):
    queryset = Dog.objects.all()
    serializer_class = DogSerializer

class DogsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Dog.objects.all()
    serializer_class = DogSerializer

class BreedsList(generics.ListCreateAPIView):
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer

class BreedsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer
