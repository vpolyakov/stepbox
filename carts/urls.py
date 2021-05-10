from django.urls import path, include
from rest_framework.routers import DefaultRouter

from carts.views import CartView, CartItemViewSet

cart_item_router = DefaultRouter()
cart_item_router.register('', CartItemViewSet, basename='cart_item')
item_patterns = cart_item_router.urls

urlpatterns = [
    path('', CartView.as_view()),
    path('items/', include(item_patterns)),
]
