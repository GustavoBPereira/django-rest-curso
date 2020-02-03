from rest_framework.serializers import ModelSerializer

from pontos_turisticos.evaluations.models import Evaluation


class EvaluationSerializer(ModelSerializer):
    class Meta:
        model = Evaluation
        fields = ('id', 'user', 'comment', 'notation', 'date')
