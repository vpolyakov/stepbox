from django.contrib.auth import get_user_model
from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView, get_object_or_404
from rest_framework.permissions import IsAuthenticated

from users.serializers import UserRegisterSerializer, CurrentUserSerializer


class UserRegisterView(CreateAPIView):
    model = get_user_model()
    serializer_class = UserRegisterSerializer


class CurrentUserRetrieveUpdateView(RetrieveUpdateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = CurrentUserSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())

        obj = get_object_or_404(queryset, id=self.request.user.id)

        # May raise a permission denied
        self.check_object_permissions(self.request, obj)

        return obj
