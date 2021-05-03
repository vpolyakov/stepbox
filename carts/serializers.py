from rest_framework import serializers

from carts.models import Cart, CartItem
from items.serializers import ItemSerializer


class CartItemSerializer(serializers.ModelSerializer):
    total_price = serializers.SerializerMethodField()
    item_id = serializers.SerializerMethodField()
    item = ItemSerializer()

    class Meta:
        model = CartItem
        fields = ('id', 'item', 'item_id', 'quantity', 'price', 'total_price')

    def get_total_price(self, obj):
        return f'{obj.price * obj.quantity:.2f}'

    def get_item_id(self, obj):
        return str(obj.item.id)


class CartItemUpdateSerializer(serializers.ModelSerializer):
    total_price = serializers.SerializerMethodField()
    item_id = serializers.IntegerField()

    class Meta:
        model = CartItem
        fields = ('id', 'item_id', 'quantity', 'price', 'total_price')

    def get_total_price(self, obj):
        return f'{obj.price * obj.quantity:.2f}'


class CartSerializer(serializers.ModelSerializer):
    cart_items = CartItemSerializer(many=True, read_only=True)  # TODO Должно быть items
    total_cost = serializers.SerializerMethodField()

    class Meta:
        model = Cart
        fields = ('id', 'cart_items', 'total_cost')

    def get_total_cost(self, obj):
        return obj.id
