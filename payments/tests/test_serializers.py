from rest_framework.test import APITestCase

from materials.models import Course
from payments.models import Payments
from payments.serializers import (
    PaymentsSerializer, SubscribeSerializer)
from users.models import User


class PaymentsSerializerTest(APITestCase):
    """
    Тестирование сериализации модели оплаты
    курса.
    """

    def setUp(self):
        self.user = User.objects.create(
            name='Test', surname='Test',
            email='test@t.com', is_superuser=True)
        self.course = Course.objects.create(
            author=self.user, name_course='Course Name',
            description='Course Description', price=1000)

    def test_valid_data(self):
        """
        Проверяет, что сериализатор
        корректно валидирует корректные данные.
        """

        payment_data = {
            "payment_user": self.user.id,
            "payment_course": self.course.id,
            "payment_amount": 100000,
            "payment_method": "transfer",

        }

        serializer = PaymentsSerializer(data=payment_data)
        self.assertTrue(serializer.is_valid())

    def test_invalid_data(self):
        """
        Проверяет, что сериализатор
        корректно валидирует некорректные данные.
        """

        payment_data = {
            "payment_user": self.user.id,
            "payment_course": '1',
            "payment_amount": "1000",
            "payment_method": "test",

        }

        serializer = PaymentsSerializer(data=payment_data)
        self.assertFalse(serializer.is_valid())


class SubscribeSerializerTest(APITestCase):
    """
    Тестирование сериализации модели подписки
    """

    def setUp(self):
        self.user = User.objects.create(
            name='Test', surname='Test',
            email='test@t.com', is_superuser=True)
        self.course = Course.objects.create(
            author=self.user, name_course='Course Name',
            description='Course Description', price=1000)
        self.payment = Payments.objects.create(
            payment_user=self.user, payment_course=self.course,
            payment_amount=100000, payment_method='transfer',
            payment_status='successes')


    def test_valid_data(self):
        """
        Проверяет, что сериализатор
        корректно валидирует корректные данные.
        """

        subscribe_data = {
            "course": self.course.id,
            "user": self.user.id
        }

        serializer = SubscribeSerializer(data=subscribe_data)
        self.assertTrue(serializer.is_valid())

    def test_is_valid_data(self):
        """
        Проверяет, что сериализатор
        корректно валидирует корректные данные.
        """

        subscribe_data = {
            "course": '1',
            "user": self.user.id
        }

        serializer = SubscribeSerializer(data=subscribe_data)
        self.assertFalse(serializer.is_valid())
