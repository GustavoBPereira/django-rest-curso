from rest_framework.serializers import ModelSerializer

from pontos_turisticos.address.models import Address


class AddressSerializer(ModelSerializer):
    class Meta:
        model = Address
        fields = ('line1', 'line2', 'city', 'state', 'country', 'lat', 'long')
