from rest_framework.routers import DefaultRouter

from reviews.views import ReviewViewSet

review_router = DefaultRouter()
review_router.register('', ReviewViewSet, basename='review')
urlpatterns = review_router.urls
