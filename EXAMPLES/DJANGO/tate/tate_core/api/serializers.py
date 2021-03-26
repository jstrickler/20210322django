from rest_framework import serializers
from tate_core.models import Artist, Artwork


class ArtworkSerializer(serializers.ModelSerializer):
    artist = serializers.HyperlinkedRelatedField(view_name='tate-api:artist-detail', read_only=True, )

    # work-in-progress:
    # artist_name = serializers.StringRelatedField(view_name='artist-detail')

    class Meta:
        model = Artwork
        fields = ('id', 'title', 'date_text', 'thumbnail_url', 'tate_url', 'artist')


class ArtistSerializer(serializers.ModelSerializer):

    # note view_name comes from router
    artworks = serializers.HyperlinkedRelatedField(view_name="tate-api:artwork-detail", many=True, read_only=True)

    class Meta:
        model = Artist
        fields = ('id', 'name', 'place_of_birth', 'birth_year', 'death_year', 'tate_url', 'artworks')
