from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from users.models import User


class UserTestCase(APITestCase):
    """
    Тестирование работы с объектом "User".
    """

    def setUp(self) -> None:
        self.user = User.objects.create(
            name='Test',
            surname='Test',
            email='test5@t.com',
            is_superuser=True,
            is_staff=True)

        self.client = APIClient()

    def test_create_user(self):
        """
        Тестирование создания пользователя
        """

        data = {
            "password": "testtestpassword",
            "name": "Test",
            "surname": "Test",
            "age": 20,
            "email": "test9@t.com",
            "phone": "83939303033",
            "country": "US",
            "city": "Test"
        }

        response_create = self.client.post(
            '/user/create/',
            data=data
        )

        self.assertEqual(
            response_create.status_code,
            status.HTTP_201_CREATED
        )

    def test_create_user_error(self):
        """
        Тестирование ошибки создания пользователя
        """

        data = {
            "password": "",
            "name": "",
            "surname": "Test",
            "age": 20,
            "email": "test9@t.com",
            "phone": "83939303033",
            "country": "US",
            "city": "Test"
        }

        response_create = self.client.post(
            '/user/create/',
            data=data
        )

        self.assertEqual(
            response_create.status_code,
            status.HTTP_400_BAD_REQUEST
        )

    def test_list_user(self):
        """
        Тестирование просмотра списка пользователей
        """
        self.client.force_authenticate(user=self.user)

        response = self.client.get(
            '/user/list/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_retrieve_user(self):
        """
        Тестирование просмотра
        информации о пользователе.
        """
        self.client.force_authenticate(user=self.user)

        response = self.client.get(
            f'/user/{self.user.id}/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_retrieve_user_current(self):
        """
        Тестирование просмотра информации о
        текущем пользователе.
        """
        self.client.force_authenticate(user=self.user)

        response = self.client.get(
            '/user/profile/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_update_user(self):
        """
        Тестирование изменения
        пользователя.
        """
        data = {
            "name": "test7499",
        }

        self.client.force_authenticate(user=self.user)

        response = self.client.patch(
            f'/user/update/{self.user.id}/',
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_delete_user(self):
        """
        Тестирование удаления пользователя
        """
        self.client.force_authenticate(user=self.user)

        response = self.client.delete(
            f'/user/delete/{self.user.id}/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

        self.assertFalse(
            User.objects.filter(id=self.user.id).exists()
        )
