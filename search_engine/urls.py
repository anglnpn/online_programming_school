from django.urls import path

from search_engine.apps import SearchEngineConfig
from search_engine.views import TextCreateAPIView, TextListAPIView, TextRetrieveAPIView, TextUpdateAPIView, \
    TextDestroyAPIView, TextSearchAPIView

app_name = SearchEngineConfig.name


urlpatterns = [
    # CRUD для текстов
    path('text/create/', TextCreateAPIView.as_view(), name='text_create'),
    path('text/list/', TextListAPIView.as_view(), name='text_list'),
    path('text/<int:pk>/', TextRetrieveAPIView.as_view(), name='text_get'),
    path('text/update/<int:pk>/', TextUpdateAPIView.as_view(), name='text_update'),
    path('text/delete/<int:pk>/', TextDestroyAPIView.as_view(), name='text_delete'),

    # Поиск по тексту
    path('text/search/', TextSearchAPIView.as_view(), name='text_search'),
              ]
