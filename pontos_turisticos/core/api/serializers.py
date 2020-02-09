from rest_framework.serializers import ModelSerializer

from pontos_turisticos.core.models import TouristSpot
from pontos_turisticos.address.api.serializers import AddressSerializer
from pontos_turisticos.comments.api.serializers import CommentSerializer
from pontos_turisticos.attractions.api.serializers import AttractionSerializer
from pontos_turisticos.evaluations.api.serializers import EvaluationSerializer


class TouristSpotSerializer(ModelSerializer):
    attractions = AttractionSerializer(many=True)
    comments = CommentSerializer(many=True)
    evaluations = EvaluationSerializer(many=True)
    address = AddressSerializer()

    class Meta:
        model = TouristSpot
        fields = (
            'id', 'name', 'description',
            'approved', 'photo', 'attractions',
            'comments', 'evaluations', 'address'
        )
