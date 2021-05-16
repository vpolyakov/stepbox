from django.db.models import Sum, F, DecimalField
from rest_framework import serializers

from carts.models import Cart, CartItem
from items.models import Item


class CartItemSerializer(serializers.ModelSerializer):
    total_price = serializers.SerializerMethodField()
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    item_id = serializers.IntegerField()

    class Meta:
        model = CartItem
        fields = (
            'id',
            'item',
            'item_id',
            'quantity',
            'price',
            'total_price',
            'user',
                  )
        extra_kwargs = {'price': {'read_only': True}}
        depth = 1

    def get_total_price(self, obj):
        return f'{obj.price * obj.quantity:.2f}'


class CartItemCreateEditSerializer(serializers.ModelSerializer):
    total_price = serializers.SerializerMethodField()
    item_id = serializers.IntegerField()

    class Meta:
        model = CartItem
        fields = (
            'id',
            'item_id',
            'quantity',
            'price',
            'total_price',
        )
        extra_kwargs = {'price': {'read_only': True}}

    def get_total_price(self, obj):
        return f'{obj.price * obj.quantity:.2f}'

    def create(self, validated_data):
        user = self.context['request'].user
        item = validated_data.get('item_id')
        cart_item = user.cart.cart_items.create(
            item_id=item,
            quantity=validated_data.get('quantity'),
            price=Item.objects.get(id=item).price,
        )
        return cart_item

    def update(self, instance, validated_data):
        item = validated_data.get('item_id')
        if item:
            instance.item_id = item
            instance.price = Item.objects.get(id=item).price

        instance.quantity = validated_data.get('quantity', instance.quantity)

        instance.save()
        return instance


class CartSerializer(serializers.ModelSerializer):
    cart_items = CartItemSerializer(many=True, read_only=True)  # TODO Должно быть items
    total_cost = serializers.SerializerMethodField()

    class Meta:
        model = Cart
        fields = (
            'id',
            'cart_items',
            'total_cost',
        )

    def get_total_cost(self, cart):
        total_cost = (
            cart.cart_items.aggregate(
                total_cost=Sum(F('price') * F('quantity'), output_field=DecimalField(max_digits=10, decimal_places=2)),
            ).get('total_cost', 0)
        )
        return f'{total_cost:.2f}' if total_cost else 0
