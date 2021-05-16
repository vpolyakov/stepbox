from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from reviews.models import Reviews
from reviews.paginators import ReviewLimitOffsetPagination
from reviews.serializers import ReviewSerializer


class CreateListModelViewSet(mixins.CreateModelMixin,
                             mixins.ListModelMixin,
                             GenericViewSet):
    """
        A viewset that provides default `create()` and `list()` actions.
        """
    pass


class ReviewViewSet(CreateListModelViewSet):
    queryset = Reviews.objects.all()
    serializer_class = ReviewSerializer
    pagination_class = ReviewLimitOffsetPagination
