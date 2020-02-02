from rest_framework.viewsets import ModelViewSet

from .serializers import AddressSerializer
from pontos_turisticos.address.models import Address


class AddressViewSet(ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
