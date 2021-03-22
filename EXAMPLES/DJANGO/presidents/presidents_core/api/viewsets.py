from rest_framework import viewsets

from presidents_core.models import Presidents
from presidents_core.api.serializers import PresidentsSerializer

# Create your viewsets here.
#
# examples:
#
class PresidentsViewSet(viewsets.ModelViewSet):
    queryset = Presidents.objects.all()
    serializer_class = PresidentsSerializer

