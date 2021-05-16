from rest_framework import serializers

from reviews.models import Reviews
from users.serializers import CurrentUserSerializer


class ReviewSerializer(serializers.ModelSerializer):
    author = CurrentUserSerializer()

    class Meta:
        model = Reviews
        fields = (
            'id',
            'author',
            'status',
            'text',
            'created_at',
            'published_at',
        )
