from rest_framework import generics, filters

from django_filters.rest_framework import DjangoFilterBackend

from materials.models import Course
from materials.permissions import IsModerPayment, IsContributor
from materials.services import convert_currencies
from payments.models import Subscribe, Payments
from payments.serializers import PaymentsSerializer, SubscribeSerializer
from payments.services import create_product, create_price, create_payment_session, get_payment_status
from users.permissions import IsUser

from rest_framework.permissions import IsAuthenticated, AllowAny

from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status

import ast


class PaymentsCreateAPIView(generics.CreateAPIView):
    """
    Создание платежа
    """

    serializer_class = PaymentsSerializer
    queryset = Payments.objects.all()
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        # получаем экземпляр сериализатора с данными POST-запроса
        serializer = self.get_serializer(data=request.data)
        # Проверяем, что данные валидны
        serializer.is_valid(raise_exception=True)

        # Получаем данные, прошедшие сериализацию
        valid_data = serializer.validated_data
        course = valid_data.get('payment_course')

        # Получаем объект курса для получения названия, цены и описания
        course_name = course.name_course
        course_description = course.description
        course_price = convert_currencies(course.price)

        # Устанавливаем значение суммы оплаты за курс
        valid_data['payment_amount'] = course_price

        # создание продукта в stripe
        product = create_product(course_name, course_description)
        # создание цены продукта в stripe
        amount = create_price(product, course_price)
        # создание сессии оплаты в stripe
        payment_session = create_payment_session(amount, success_url='https://example.com/success',
                                                 cancel_url='https://example.com/cancel')

        # Добавляем ссылку на оплату в данные о платеже
        valid_data['payment_session_id'] = payment_session

        # Создаем объект платежа в базе данных
        self.perform_create(serializer)

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class PaymentStatusAPIView(generics.CreateAPIView):
    """
    Получение статуса оплаты
    В пост запрос передается payments_id.
    Контроллер передает его в сервисную функцию.
    Функция делает запрос в stripe и получает статус оплаты.
    """

    serializer_class = PaymentsSerializer
    queryset = Payments.objects.all()
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        payment_id = request.data.get('payment_id')

        payment_obj = Payments.objects.get(id=payment_id)

        pay_session_str = payment_obj.payment_session_id
        pay_session_dict = ast.literal_eval(pay_session_str)

        session_id = pay_session_dict.get('session_id')

        payment_status = get_payment_status(session_id)

        if payment_status == 'complete':
            payment_obj.payment_status = 'Успешно'
            payment_obj.save()
        else:
            payment_obj.payment_status = 'Неуспешно'
            payment_obj.save()

        return Response({'payment_status': payment_status}, status=status.HTTP_200_OK)


class PaymentsListAPIView(generics.ListAPIView):
    """
    Вывод списка платежей.
    Подключена фильтрация по курсу, способу оплаты
    и дате.
    """
    serializer_class = PaymentsSerializer
    queryset = Payments.objects.all()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['payment_course']
    search_fields = ['payment_method']
    ordering_fields = ['payment_date']
    permission_classes = [IsAuthenticated, IsModerPayment]


class PaymentsRetrieveAPIView(generics.RetrieveAPIView):
    """
    Просмотр платежа
    """
    serializer_class = PaymentsSerializer
    queryset = Payments.objects.all()
    permission_classes = [IsAuthenticated, IsModerPayment | IsContributor]


class SubscribeCreateAPIView(generics.CreateAPIView):
    """
    Cоздание подписки
    """
    serializer_class = SubscribeSerializer
    queryset = Subscribe.objects.all()
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        user = self.request.user
        course_id = self.request.data.get('course_id')

        course_item = get_object_or_404(Course, id=course_id)
        payment = Payments.objects.filter(
            payment_user=user,
            payment_course=course_id,
            payment_status='Успешно')
        # Проверяем, что пользователь оплатил курс
        if payment:
            # Получаем объект подписки по пользователю курсу
            subs_item = Subscribe.objects.filter(
                user=user,
                course=course_item)

            # Если подписка у пользователя на этот курс есть - удаляем ее
            if subs_item:
                subs_item.delete()
                message = 'подписка удалена'
            # Если подписки у пользователя на этот курс нет - создаем ее
            else:
                subscribe_new = Subscribe.objects.create(
                    user=user,
                    course=course_item)
                subscribe_new.save()
                message = 'подписка добавлена'
            # Возвращаем ответ в API
            return Response({"message": message})
        else:
            return Response({"message": 'Вы не оплатили данный курс'})
