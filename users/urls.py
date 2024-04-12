from django.urls import path

from users.apps import UsersConfig

from users.views import UserCreateAPIView, \
    UserListAPIView, \
    UserRetrieveAPIView, \
    UserUpdateAPIView, \
    UserDestroyAPIView, \
    CurrentUserRetrieveAPIView


app_name = UsersConfig.name


urlpatterns = [
    path('create/', UserCreateAPIView.as_view(), name='user_create'),
    path('list/', UserListAPIView.as_view(), name='user_list'),
    path('profile/', CurrentUserRetrieveAPIView.as_view(), name='user_get'),
    path('update/<int:pk>/', UserUpdateAPIView.as_view(), name='user_update'),
    path('delete/<int:pk>/', UserDestroyAPIView.as_view(), name='user_delete'),
    path('<int:pk>/', UserRetrieveAPIView.as_view(), name='user_get'),
    path('update/<int:pk>/', UserUpdateAPIView.as_view(), name='user_update'),
    path('delete/<int:pk>/', UserDestroyAPIView.as_view(), name='user_delete'),
              ]
