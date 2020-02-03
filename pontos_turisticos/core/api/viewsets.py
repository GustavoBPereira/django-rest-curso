from rest_framework.viewsets import ModelViewSet

from .serializers import TouristSpotSerializer
from pontos_turisticos.core.models import TouristSpot


class TouristSpotViewSet(ModelViewSet):
    serializer_class = TouristSpotSerializer

    def get_queryset(self):
        return TouristSpot.objects.filter(approved=True)
