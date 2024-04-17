from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from rest_framework import generics, status
from rest_framework.response import Response

from search_engine.paginators import TextPagination
from search_engine.permissions import IsTextModer
from search_engine.serializers import TextSerializer
from search_engine.models import Text
from search_engine.utils import TextDocument

import logging

logging.basicConfig(level=logging.INFO)


class TextCreateAPIView(generics.CreateAPIView):
    """
    Cоздание текста
    """
    serializer_class = TextSerializer
    queryset = Text.objects.all()
    permission_classes = [IsAuthenticated, IsTextModer]


class TextListAPIView(generics.ListAPIView):
    """
    Просмотр списка текстов
    """
    serializer_class = TextSerializer
    queryset = Text.objects.all()
    permission_classes = [AllowAny]
    pagination_class = TextPagination


class TextRetrieveAPIView(generics.RetrieveAPIView):
    """
    Просмотр одного текста
    """
    serializer_class = TextSerializer
    queryset = Text.objects.all()
    permission_classes = [AllowAny]


class TextUpdateAPIView(generics.UpdateAPIView):
    """
    Изменение текста
    """
    serializer_class = TextSerializer
    queryset = Text.objects.all()
    permission_classes = [AllowAny]


class TextDestroyAPIView(generics.DestroyAPIView):
    """
    Удаление текста
    """
    queryset = Text.objects.all()
    permission_classes = [AllowAny]


class TextSearchAPIView(APIView):
    """
    Поиск по текстам через query-запрос
    """

    def post(self, request):
        hits_list = []
        query = request.data.get('query')

        logging.info(f"request '{request}'.")
        logging.info(f"request.data '{request.data}'.")
        logging.info(f"Начался поиск точных совпадений по запросу '{query}'.")

        if query:
            search_results = TextDocument.search().query(
                "match", text=query).extra(size=2)

            for hit in search_results:
                print(
                    "Рубрика: {}, тема: {}, текст: {}".format(
                        hit.rubrics, hit.theme, hit.text)
                )
                hits_dict = {
                    'Рубрика': hit.rubrics,
                    'Тема': hit.theme,
                    'Текст': hit.text}
                hits_list.append(hits_dict)

            if not hits_list:
                logging.info(
                    f'Точных совпадений по запросу "{query}" не нашлось.')
                data = {'Сообщение': f'Точных совпадений по запросу '
                                     f'"{query}" не нашлось.', 'hits': []}
                return Response(data, status=status.HTTP_404_NOT_FOUND)
            else:
                logging.info(
                    f'По запросу слова "{query}" '
                    f'были выведены следующие совпадения: {hits_list}')
                data = {'Сообщение': f'По запросу слова "{query}" '
                                     f'были выведены следующие совпадения: ',
                        'hits': hits_list}
                return Response(data, status=status.HTTP_200_OK)

        else:
            return Response({'Ошибка': 'Требуется параметр запроса "query".'},
                            status=status.HTTP_400_BAD_REQUEST)


