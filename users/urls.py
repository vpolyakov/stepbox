from django.urls import path
from rest_framework.authtoken import views

from users.views import UserRegisterView, CurrentUserRetrieveUpdateView

urlpatterns = [
    path('auth/login', views.obtain_auth_token),
    path('auth/register', UserRegisterView.as_view()),
    path('current', CurrentUserRetrieveUpdateView.as_view()),
]
