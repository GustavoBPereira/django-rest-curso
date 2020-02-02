from rest_framework.viewsets import ModelViewSet

from .serializers import AttractionSerializer
from pontos_turisticos.attractions.models import Attraction


class AttractionViewSet(ModelViewSet):
    queryset = Attraction.objects.all()
    serializer_class = AttractionSerializer
