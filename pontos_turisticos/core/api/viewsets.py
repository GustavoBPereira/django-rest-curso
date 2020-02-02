from rest_framework.viewsets import ModelViewSet

from .serializers import TouristSpotSerializer
from pontos_turisticos.core.models import TouristSpot


class TouristSpotViewSet(ModelViewSet):
    queryset = TouristSpot.objects.all()
    serializer_class = TouristSpotSerializer
