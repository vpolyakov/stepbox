from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.filters import OrderingFilter
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet

from items.filters import ItemFilter
from items.models import Item
from items.paginators import ItemPageNumberPagination
from items.serializers import ItemSerializer


class ItemViewSet(ReadOnlyModelViewSet):  # ModelViewSet
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    pagination_class = ItemPageNumberPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = ItemFilter
    ordering = ['title', 'price', 'weight']
    ordering_fields = ['title', 'price', 'weight']


@api_view(http_method_names=['GET'])
def get_item_view(request, pk):
    try:
        item = Item.objects.get(pk=pk)
        return Response({
            'id': item.id,
            'title': item.title,
            'description': item.description,
            'image': request.build_absolute_uri(item.image.url),
            'weight': item.weight,
            'price': f'{item.price:.2f}',
        })
    except Item.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
