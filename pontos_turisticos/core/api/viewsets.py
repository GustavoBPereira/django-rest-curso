from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet

from .serializers import TouristSpotSerializer
from pontos_turisticos.core.models import TouristSpot


class TouristSpotViewSet(ModelViewSet):
    serializer_class = TouristSpotSerializer
    filterset_fields = ['name']
    filter_backends = (SearchFilter,)
    search_fields = ['name', 'description']

    def get_queryset(self):
        return TouristSpot.objects.all()

    def list(self, request, *args, **kwargs):
        return super(TouristSpotViewSet, self).list(request, *args, **kwargs)

    @action(methods=['get'], detail=True)
    def denounce(self, request, pk=None):
        pass
