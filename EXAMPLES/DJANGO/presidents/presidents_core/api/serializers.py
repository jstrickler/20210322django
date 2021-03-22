from rest_framework import serializers
from presidents_core.models import Presidents  # change to only needed models

class PresidentsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Presidents
        fields = (
            'termnum', 'firstname', 'lastname', 'birthdate', 'deathdate',
            'birthplace', 'birthstate', 'termstart', 'termend', 'party'
        )
