from rest_framework.viewsets import ModelViewSet

from .serializers import CommentSerializer
from pontos_turisticos.comments.models import Comment


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
