from rest_framework.test import APITestCase, APIClient
from rest_framework import status

from users.models import User

from search_engine.models import Text


class UserTestCase(APITestCase):
    """
    Тестирование работы с пользователем.
    """

    def setUp(self) -> None:
        self.user = User.objects.create(
            name='Test',
            surname='Test',
            email='test_usachev@sky.com',
            is_superuser=True,
            is_staff=True
        )

        self.text = Text.objects.create(
            id=2,
            rubrics='Введение в Django',
            theme='Тест темы',
            text='Тест текста',
            created_date='2024-04-01 21:35:07.891282+05'
        )

        self.client = APIClient()

    def test_create_text(self):
        """
        Тестирование создания текста
        """

        data = {
            "id": 1,
            "rubrics": "Введение в Django",
            "theme": "Тест темы",
            "text": "Тест текста",
            "created_date": "2024-04-01 21:35:07.891282+05",
        }
        self.client.force_authenticate(user=self.user)

        response = self.client.post(
            '/search_engine/text/create/',
            data=data
        )
        print(response.json())
        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )
        # Проверяем, что пользователь действительно создан
        created_user = User.objects.get(email='test_usachev@sky.com')
        self.assertIsNotNone(created_user)

    def test_list_user(self):
        """
        Тестирование просмотра списка текстов
        """
        self.client.force_authenticate(user=self.user)

        response = self.client.get(
            '/search_engine/text/list/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_retrieve_user(self):
        """
        Тестирование просмотра одного текста
        """
        self.client.force_authenticate(user=self.user)

        response = self.client.get(
            f'/search_engine/text/{self.text.id}/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_update_user(self):
        """
        Тестирование изменения текста
        """
        data = {
            "text": "Измененный текст",
        }

        self.client.force_authenticate(user=self.user)

        response = self.client.patch(
            f'/search_engine/text/update/{self.text.id}/',
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_delete_user(self):
        """
        Тестирование удаление текста
        """
        self.client.force_authenticate(user=self.user)

        response = self.client.delete(
            f'/search_engine/text/delete/{self.text.id}/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

    def test_search_text(self):
        """
        Тестирование поиска текста
        """

        data = {
            'query': 'текста',
        }
        print(f'{data}')

        response = self.client.post(
            '/search_engine/text/search/',
            data=data,
            format='json'
        )

        print(response)

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_search_text_not_found(self):
        """
        Проверка поиска текста при отсутствии совпадений
        """
        data = {
            'query': 'несуществующий текст',
        }

        response = self.client.post(
            '/search_engine/text/search/',
            data=data,
            format='json'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_404_NOT_FOUND
        )
