from rest_framework import generics
from users.models import User
from users.paginators import UserPagination
from users.permissions import IsUser
from users.serializers import UserSerializer, LimitedUserSerializer
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.hashers import make_password


class UserCreateAPIView(generics.CreateAPIView):
    """
    Cоздание пользователя
    """
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def perform_create(self, serializer):
        """
        Хэширование пароля перед
        сохранением пользователя.
        """
        validated_data = serializer.validated_data
        password = validated_data.get('password')
        hashed_password = make_password(password)
        serializer.save(password=hashed_password)


class UserListAPIView(generics.ListAPIView):
    """
    Просмотр списка пользователей
    """
    queryset = User.objects.all()
    serializer_class = LimitedUserSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = UserPagination

    def get(self, request):
        queryset = User.objects.all()
        paginated_queryset = self.paginate_queryset(queryset)
        serializer = LimitedUserSerializer(
            paginated_queryset, many=True)
        return self.get_paginated_response(serializer.data)


class UserRetrieveAPIView(generics.RetrieveAPIView):
    """
    Просмотр одного пользователя
    """
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        """
        Возвращает экземпляр сериализатора,
        который будет использован для отображения
        данного объекта пользователя.
        Персонал видит все поля пользователя,
        а обычный пользователь с ограничениями.
        """
        if self.request.user.is_staff:
            return UserSerializer
        else:
            return LimitedUserSerializer


class UserUpdateAPIView(generics.UpdateAPIView):
    """
    Изменение пользователя
    """
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated, IsUser]


class UserDestroyAPIView(generics.DestroyAPIView):
    """
    Удаление пользователя
    """
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated, IsUser]


class CurrentUserRetrieveAPIView(generics.RetrieveAPIView):
    """
    Получение информации о текущем пользователе.
    """
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsUser]

    def get_object(self) -> User:
        """
        Возвращает текущего
        аутентифицированного пользователя.
        """
        return self.request.user
