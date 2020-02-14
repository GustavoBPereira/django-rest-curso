from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from pontos_turisticos.address.models import Address
from pontos_turisticos.attractions.models import Attraction
from pontos_turisticos.core.models import TouristSpot
from pontos_turisticos.address.api.serializers import AddressSerializer
from pontos_turisticos.comments.api.serializers import CommentSerializer
from pontos_turisticos.attractions.api.serializers import AttractionSerializer
from pontos_turisticos.evaluations.api.serializers import EvaluationSerializer


class TouristSpotSerializer(ModelSerializer):
    attractions = AttractionSerializer(many=True)
    comments = CommentSerializer(many=True, read_only=True)
    evaluations = EvaluationSerializer(many=True, read_only=True)
    address = AddressSerializer()
    full_description = SerializerMethodField()

    class Meta:
        model = TouristSpot
        fields = (
            'id', 'name', 'description',
            'approved', 'photo', 'attractions',
            'comments', 'evaluations', 'address',
            'full_description'
        )
        read_only_fields = ('photo',)

    def create_attractions(self, attractions, spot):
        for attraction in attractions:
            at = Attraction.objects.create(**attraction)
            spot.attractions.add(at)

    def create(self, validated_data):
        attractions = validated_data['attractions']
        del validated_data['attractions']

        address = validated_data['address']
        del validated_data['address']

        spot = TouristSpot.objects.create(**validated_data)
        self.create_attractions(attractions, spot)

        _address = Address.objects.create(**address)
        spot.address = _address

        return spot

    def get_full_description(self, obj):
        return f'{obj.description} - {obj.name}'
