from datetime import datetime

from rest_framework.test import APITestCase, force_authenticate
from rest_framework import status

from materials.models import Course
from payments.models import Payments
from users.models import User


class SubscribeTestCase(APITestCase):
    """
    Тестирование подписки.
    """

    def setUp(self) -> None:
        self.user = User.objects.create(name='Test', surname='Test', email='test@t.com', is_superuser=True)
        self.course = Course.objects.create(name_course='Course Name', description='Course Description', price=100)

    def test_create_subscribe(self):
        """
        Тестирование создания и удаления подписки.
        Создание и удаления происходят в одном эндпоинте.
        Для выполнения передаются id курса и id пользователя.
        """
        data = {
            'course_id': self.course.id,
            'user_id': self.user.id
        }

        self.client.force_authenticate(user=self.user)

        response_create = self.client.post(
            '/payments/subscribe_create/',
            data=data
        )

        response_delete = self.client.post(
            '/payments/subscribe_create/',
            data=data
        )

        self.assertEqual(
            response_create.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response_delete.status_code,
            status.HTTP_200_OK
        )


class PaymentsTestCase(APITestCase):
    """
    Тестирование оплаты.
    """

    def setUp(self) -> None:
        self.user = User.objects.create(name='Test', surname='Test', email='test@t.com', is_superuser=True)
        self.course = Course.objects.create(name_course='Course Name', description='Course Description', price=100)
        self.course_2 = Course.objects.create(name_course='Course Name', description='Course Description', price=100)
        self.payments = Payments.objects.create(payment_user=self.user,
                                                payment_date=datetime.now(),
                                                payment_course=self.course,
                                                payment_amount=1000000,
                                                payment_session_id='123456789012345',
                                                payment_status='successes')
        self.payments_2 = Payments.objects.create(payment_user=self.user,
                                                  payment_date=datetime.now(),
                                                  payment_course=self.course_2,
                                                  payment_amount=1000000,
                                                  payment_session_id='123456789012345',
                                                  payment_status='successes')

    def test_create_payments(self):
        """
        Тестирование создания оплаты
        """
        data = {
            'payment_course': self.course.id,
            'payment_user': self.user.id,
            'payment_amount': 1000000,
            'payment_method': 'transfer',
        }

        self.client.force_authenticate(user=self.user)


