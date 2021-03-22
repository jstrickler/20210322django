from rest_framework import serializers
from dogs_core.models import Dog, Breed

class BreedSerializerX(serializers.Serializer):

    id = serializers.UUIDField()
    name = serializers.CharField(max_length=32)
    abbr = serializers.CharField(max_length=8)

class DogSerializerX(serializers.Serializer):

    id = serializers.UUIDField()
    name = serializers.CharField(max_length=32)
    weight = serializers.IntegerField()
    sex = serializers.CharField(max_length=2)
    breed = BreedSerializerX()
    is_neutered = serializers.BooleanField()


class BreedSerializer(serializers.ModelSerializer):

    class Meta:
        model = Breed
        fields = ('id', 'name', 'abbr')

class DogSerializer(serializers.ModelSerializer):
    breed = serializers.HyperlinkedRelatedField(view_name='dogs_core:api:breeds-detail-cbv', read_only=True)

    class Meta:
        model = Dog
        fields = ('id', 'name', 'breed', 'weight', 'sex', 'is_neutered')

