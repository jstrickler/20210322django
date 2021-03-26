from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from tate_core.models import Artist, Artwork
from tate_core.api.serializers import ArtistSerializer, ArtworkSerializer
from tate_core.api.filters import ArtistFilter, ArtworkFilter


class ArtistViewSet(viewsets.ModelViewSet):
    """
     retrieve:
     Return the given artist.

     list:
     Return a list of all artists.

     create:
     Create a new artist instance.
     """
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ArtistFilter

class ArtworkViewSet(viewsets.ModelViewSet):
    """
     retrieve:
     Return the given artwork.

     list:
     Return a list of all artworks.

     create:
     Create a new artwork instance.
     """
    queryset = Artwork.objects.all()
    serializer_class = ArtworkSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ArtworkFilter

