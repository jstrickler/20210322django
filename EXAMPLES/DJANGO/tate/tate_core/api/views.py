from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from tate_core.models import Artist, Artwork
from tate_core.api.serializers import ArtistSerializer, ArtworkSerializer
from tate_core.api.filters import ArtistFilter, ArtworkFilter

# function-based views (aka FBVs)

@api_view()
def hello_world(request):
    """
    Trivial REST resource

    :param request:
    :return:
    """
    return Response({"message": "Hello, world!"})

@api_view(['GET'])
def artists(request, guid):
    """
    Function-based view to retrieve one artist.

    :param request:
    :param guid:
    :return:
    """
    if request.method == 'GET':
        artist = get_object_or_404(Artist, id=guid)
        serializer = ArtistSerializer(artist, context={'request': request})
        return Response(serializer.data)

# class-based views (aka CBVs)
class ArtistsList(generics.ListCreateAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ArtistFilter


class ArtistsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ArtistFilter

# class-based views (aka CBVs)
class ArtworksList(generics.ListCreateAPIView):
    queryset = Artwork.objects.all()
    serializer_class = ArtworkSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ArtworkFilter


class ArtistsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Artwork.objects.all()
    serializer_class = ArtworkSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ArtworkFilter

