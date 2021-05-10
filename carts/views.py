from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from carts.paginators import CartItemLimitOffsetPagination
from carts.serializers import CartSerializer, CartItemSerializer, CartItemCreateEditSerializer


class CartView(RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = CartSerializer

    def get_object(self):
        cart = self.request.user.cart

        # May raise a permission denied
        self.check_object_permissions(self.request, cart)

        return cart


class CartItemViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    pagination_class = CartItemLimitOffsetPagination
    serializer_class = CartItemSerializer

    def get_queryset(self):
        return self.request.user.cart.cart_items.all()

    def get_serializer_class(self):
        if self.request._request.method in ['POST', 'PUT', 'PATCH']:
            return CartItemCreateEditSerializer
        else:
            return CartItemSerializer
