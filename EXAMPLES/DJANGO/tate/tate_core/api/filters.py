from django_filters import rest_framework as filters
from tate_core.models import Artist, Artwork

class ArtistFilter(filters.FilterSet):
    name = filters.CharFilter(field_name="name", lookup_expr='icontains')
    birthplace = filters.CharFilter(field_name="place_of_birth", lookup_expr='icontains')

    min_birth_year = filters.NumberFilter(field_name="birth_year", lookup_expr='gte')

    max_birth_year = filters.NumberFilter(field_name="birth_year", lookup_expr='lte')

    min_death_year = filters.NumberFilter(field_name="death_year", lookup_expr='gte')
    max_death_year = filters.NumberFilter(field_name="death_year", lookup_expr='lte')

    alive = filters.BooleanFilter(field_name="death_year", lookup_expr='isnull')


    class Meta:
        model = Artist
        fields = ['name', 'birthplace', 'min_birth_year', 'max_death_year',
                  'min_death_year', 'max_death_year', 'alive']

class ArtworkFilter(filters.FilterSet):
    title = filters.CharFilter(field_name="title", lookup_expr='icontains')

    class Meta:
        model = Artwork
        fields = ['title']
