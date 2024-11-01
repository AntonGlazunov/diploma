from rest_framework import generics
from rest_framework.permissions import AllowAny

from users.models import User
from users_api.permissions import IsOwner
from users_api.serializers import UserSerializer, UserCreateSerializer, UserPreferencesSerializer, \
    MovieStatisticSerializer


class UserCreateAPIView(generics.CreateAPIView):
    serializer_class = UserCreateSerializer
    queryset = User.objects.all()
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()


class UserListAPIView(generics.ListAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsOwner]

    def get_queryset(self):
        queryset = User.objects.filter(pk=self.request.user.pk)
        return queryset

class UserRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsOwner]


class UserUpdateAPIView(generics.UpdateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsOwner]


class UserDestroyAPIView(generics.DestroyAPIView):
    queryset = User.objects.all()
    permission_classes = [IsOwner]


class UserPreferencesUpdateAPIView(generics.UpdateAPIView):
    serializer_class = UserPreferencesSerializer
    queryset = User.objects.all()
    permission_classes = [IsOwner]


class UserPreferencesRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = UserPreferencesSerializer
    queryset = User.objects.all()
    permission_classes = [IsOwner]

class UserStatisticsRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = MovieStatisticSerializer
    queryset = User.objects.all()
    permission_classes = [IsOwner]
