from rest_framework.serializers import ModelSerializer

from pontos_turisticos.core.models import TouristSpot


class TouristSpotSerializer(ModelSerializer):

    class Meta:
        model = TouristSpot
        fields = ('id', 'name', 'description', 'approved', 'photo')
