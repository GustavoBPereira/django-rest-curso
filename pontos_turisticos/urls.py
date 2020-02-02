from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from pontos_turisticos.attractions.api.viewsets import AttractionViewSet
from pontos_turisticos.core.api.viewsets import TouristSpotViewSet
from pontos_turisticos.address.api.viewsets import AddressViewSet

router = routers.DefaultRouter()
router.register(r'touristspot', TouristSpotViewSet)
router.register(r'attractions', AttractionViewSet)
router.register(r'addresses', AddressViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
