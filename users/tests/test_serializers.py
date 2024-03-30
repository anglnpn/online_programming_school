from rest_framework.test import APITestCase

from users.serializers import UserSerializer, LimitedUserSerializer


class UserSerializerTest(APITestCase):
    """
    Тестирование сериализации модели пользователя.
    """

    def test_valid_data(self):
        """
        Проверяет, что сериализатор
        корректно валидирует корректные данные.
        """

        user_data = {
            "name": "Test",
            "surname": "Test",
            "email": "test234@tu.com",
            "password": "test123",
            "age": 23,
            "country": "Russia",
            "city": "Moscow",
        }

        serializer = UserSerializer(data=user_data)
        self.assertTrue(serializer.is_valid())

    def test_invalid_data(self):
        """
        Проверяет, что сериализатор
        корректно валидирует некорректные данные.
        """

        user_data = {
            "name": "",
            "surname": "Test",
            "email": "test234@tu.com",
            "password": "",
        }

        serializer = UserSerializer(data=user_data)
        self.assertFalse(serializer.is_valid())


class LimitUserSerializerTest(APITestCase):
    """
    Тестирование сериализации модели пользователя
    с ограниченным выводом полей.
    """
    def test_valid_data(self):
        """
        Проверяет, что сериализатор
        корректно валидирует корректные данные.
        """

        user_data = {
            "name": "Test",
            "age": 23,
            "city": "Moscow",
        }

        serializer = LimitedUserSerializer(data=user_data)
        self.assertTrue(serializer.is_valid())

    def test_invalid_data(self):
        """
        Проверяет, что сериализатор
        корректно валидирует некорректные данные.
        """

        user_data = {
            "name": "",
            "avatar": "https://images",
            "age": 23,
            "city": "Moscow",
        }

        serializer = LimitedUserSerializer(data=user_data)
        self.assertFalse(serializer.is_valid())
