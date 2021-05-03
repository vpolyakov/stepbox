from rest_framework.routers import DefaultRouter

from items.views import ItemViewSet

item_router = DefaultRouter()
item_router.register('', ItemViewSet, basename='item')
urlpatterns = item_router.urls
