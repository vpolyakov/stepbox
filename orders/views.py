from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet

from orders.models import Order
from orders.paginators import OrderLimitOffsetPagination
from orders.serializers import OrderSerializer


class CreateRetrieveUpdateListModelViewSet(mixins.CreateModelMixin,
                                           mixins.RetrieveModelMixin,
                                           mixins.UpdateModelMixin,
                                           mixins.ListModelMixin,
                                           GenericViewSet):
    """
    A viewset that provides default `create()`, `retrieve()`, `update()`,
    `partial_update()` and `list()` actions.
    """
    pass


class OrderViewSet(CreateRetrieveUpdateListModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    pagination_class = OrderLimitOffsetPagination
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        queryset = self.request.user.orders.all()
        return queryset
