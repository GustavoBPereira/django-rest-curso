from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet

from .serializers import TouristSpotSerializer
from pontos_turisticos.core.models import TouristSpot


class TouristSpotViewSet(ModelViewSet):
    serializer_class = TouristSpotSerializer

    def get_queryset(self):
        _id = self.request.query_params.get('id')
        queryset = TouristSpot.objects.all()
        if _id:
            queryset = queryset.filter(pk=_id)
        return queryset

    def list(self, request, *args, **kwargs):
        return super(TouristSpotViewSet, self).list(request, *args, **kwargs)

    @action(methods=['get'], detail=True)
    def denounce(self, request, pk=None):
        pass
