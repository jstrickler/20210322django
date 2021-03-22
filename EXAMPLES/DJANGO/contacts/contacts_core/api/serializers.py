from rest_framework import serializers
from contacts_core.models import City, Contact


class AnimalSerializer(serializers.Serializer):

    animal = serializers.CharField(max_length=32)
    country = serializers.CharField(max_length=32)

class CitySerializerPlain(serializers.Serializer):

    id = serializers.UUIDField()
    name = serializers.CharField(max_length=32)
    admindiv = serializers.CharField(max_length=32)
    country = serializers.CharField(max_length=2)

class ContactSerializerPlain(serializers.Serializer):

    id = serializers.UUIDField()
    first_name = serializers.CharField(max_length=32)
    last_name = serializers.CharField(max_length=32)
    street_address = serializers.CharField(max_length=32)
    postcode = serializers.CharField(max_length=16)
    dob = serializers.DateField()
    city = CitySerializerPlain()

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ('id', 'name', 'admindiv', 'country')

class ContactSerializer(serializers.ModelSerializer):
    city = serializers.HyperlinkedRelatedField(view_name='contacts_core:api:city-detail', read_only=True)

    class Meta:
        model = Contact
        fields = ('id', 'first_name', 'last_name', 'street_address', 'city', 'postcode', 'dob')


