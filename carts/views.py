from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from carts.models import Cart, CartItem
from carts.paginators import CartItemLimitOffsetPagination
from carts.serializers import CartSerializer, CartItemSerializer, CartItemUpdateSerializer


class CartListView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = CartSerializer

    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)


class CartItemViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    pagination_class = CartItemLimitOffsetPagination

    def get_queryset(self):
        return CartItem.objects.filter(cart=self.request.user.cart())

    def get_serializer_class(self):
        if self.request._request.method in ['PUT', 'PATCH']:
            return CartItemUpdateSerializer
        else:
            return CartItemSerializer
