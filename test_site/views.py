import logging

from rest_framework import generics
from rest_framework.permissions import IsAdminUser

from test_site.models import User
from test_site.permissions import IsSelfOrAdmin
from test_site.serializers import UserSerializer
logger = logging.getLogger('main')


# Пользователи
# Представление для обновления информации о пользователе
class UserUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsSelfOrAdmin,)


# Представление для удаления пользователя
class UserDeleteAPIView(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsSelfOrAdmin,)

    def perform_delete(self, serializer):
        user = serializer.save()
        logger.info('User %s deleted', user.pk)


# Представление для создания нового пользователя
class UserCreateAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdminUser,)


# Представление для списка пользователей
class UserListAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdminUser,)
