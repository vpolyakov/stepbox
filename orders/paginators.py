from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination


class OrderPageNumberPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 4


class OrderLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 2
    max_limit = 4
