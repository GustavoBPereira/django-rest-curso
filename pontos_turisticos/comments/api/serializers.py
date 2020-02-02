from rest_framework.serializers import ModelSerializer

from pontos_turisticos.comments.models import Comment


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'user', 'comment', 'date', 'approved')
