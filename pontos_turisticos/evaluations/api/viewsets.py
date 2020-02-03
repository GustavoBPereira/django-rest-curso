from rest_framework.viewsets import ModelViewSet

from .serializers import EvaluationSerializer
from pontos_turisticos.evaluations.models import Evaluation


class EvaluationViewSet(ModelViewSet):
    queryset = Evaluation.objects.all()
    serializer_class = EvaluationSerializer
