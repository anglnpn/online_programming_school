from rest_framework import generics, filters

from django_filters.rest_framework import DjangoFilterBackend

from course_materials.models import Course
from course_materials.services import convert_currencies

from payments.models import Subscribe, Payments
from payments.permissions import IsModerPayment, IsContributor
from payments.serializers import PaymentsSerializer, SubscribeSerializer
from payments.services import (create_product,
                               create_price,
                               create_payment_session)


from rest_framework.permissions import IsAuthenticated

from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status



class PaymentsCreateAPIView(generics.CreateAPIView):
    """
    Создание платежа
    """

    serializer_class = PaymentsSerializer
    queryset = Payments.objects.all()
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs) -> Response:
        # получаем экземпляр сериализатора с данными POST-запроса
        serializer = self.get_serializer(data=request.data)
        # Проверяем, что данные валидны
        serializer.is_valid(raise_exception=True)

        # Получаем текущего пользователя
        user = self.request.user

        # Получаем данные, прошедшие сериализацию
        valid_data = serializer.validated_data
        course = valid_data.get('payment_course')

        # Записываем текущего пользователя в поле payment_user
        valid_data['payment_user'] = user

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
        payment_session = create_payment_session(
            amount, success_url='http://localhost:3000/user_courses',
            cancel_url='https://example.com/cancel')

        # Добавляем ссылку на оплату в данные о платеже
        valid_data['payment_session_id'] = payment_session

        # Создаем объект платежа в базе данных
        self.perform_create(serializer)

        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class PaymentsListAPIView(generics.ListAPIView):
    """
    Вывод списка платежей.
    Подключена фильтрация по курсу, способу оплаты
    и дате.
    """
    serializer_class = PaymentsSerializer
    queryset = Payments.objects.all()
    filter_backends = [DjangoFilterBackend,
                       filters.SearchFilter,
                       filters.OrderingFilter]
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
    permission_classes = [IsAuthenticated,
                          IsModerPayment | IsContributor]


class SubscribeCreateAPIView(generics.CreateAPIView):
    """
    Cоздание подписки
    """
    serializer_class = SubscribeSerializer
    queryset = Subscribe.objects.all()
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs) -> Response:
        user = self.request.user
        print(user)
        course_id = self.request.data.get('course_id')
        print(course_id)

        course_item = get_object_or_404(Course, id=course_id)
        payment = Payments.objects.filter(
            payment_user=user,
            payment_course=course_id,
            payment_status='successes')
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
