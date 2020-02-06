from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken.views import obtain_auth_token

from pontos_turisticos.attractions.api.viewsets import AttractionViewSet
from pontos_turisticos.core.api.viewsets import TouristSpotViewSet
from pontos_turisticos.address.api.viewsets import AddressViewSet
from pontos_turisticos.comments.api.viewsets import CommentViewSet
from pontos_turisticos.evaluations.api.viewsets import EvaluationViewSet

router = routers.DefaultRouter()
router.register(r'touristspots', TouristSpotViewSet, basename='TouristSpot')
router.register(r'attractions', AttractionViewSet)
router.register(r'addresses', AddressViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'evaluations', EvaluationViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-token-auth/', obtain_auth_token),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
