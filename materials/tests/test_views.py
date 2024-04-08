from rest_framework.test import APITestCase
from rest_framework import status

from materials.models import Course, Lesson, Module

from users.models import User


class LessonTestCase(APITestCase):
    """
    Тест для урока.
    """

    def setUp(self) -> None:
        # Создание объектов для тестирования
        self.user = User.objects.create(
            name='Test', surname='Test', email='test@t.com',
            is_superuser=True)
        self.course = Course.objects.create(
            author=self.user, name_course='Course Name',
            description='Course Description', price=1000)
        self.module = Module.objects.create(
            author=self.user, course_id=self.course, sequence_number=1,
            name_module='Module Name', description='Module Description')
        self.lesson = Lesson.objects.create(
            name_lesson='Lesson Name', description='List Description',
            link='https://my.sky.pro/youtube.com', module_id=self.module,
            author=self.user)

    def test_create_lesson(self):
        """
        Тестирование создания урока
        """
        data = {
            'name_lesson': 'Test',
            'description': 'Test',
            'link': 'https://my.sky.pro/youtube.com',
            'module_id': self.module.id,
            'content': 'Test content',
            'author': self.user.id
        }
        self.client.force_authenticate(user=self.user)

        response = self.client.post(
            '/lesson/create/',
            data=data
        )
        print(response.json())

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

    def test_list_lesson(self):
        """
        Тестирование просмотра списка уроков
        """
        self.client.force_authenticate(user=self.user)

        response = self.client.get(
            '/lesson/'
        )
        print(response.json())

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_retrieve_lesson(self):
        """
        Тестирование просмотра одного урока
        """
        self.client.force_authenticate(user=self.user)
        print(self.lesson.id)

        response = self.client.get(
            f'/lesson/{self.lesson.id}/'
        )
        print(response.json())

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_update_lesson(self):
        """
        Тестирование изменение урока
        """
        self.client.force_authenticate(user=self.user)

        data = {
            "name_lesson": "test4555",
            "link": "https://youtube.com",
            "description": "test description",
            "module_id": self.module.id,
            "content": "test content",
            "author": self.user.id
        }

        response = self.client.put(
            f'/lesson/update/{self.lesson.id}/',
            data=data
        )
        print(response.json())

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        print(response.status_code)

    def test_delete_lesson(self):
        """
        Тестирование удаление урока
        """

        self.client.force_authenticate(user=self.user)

        response = self.client.delete(
            f'/lesson/delete/{self.lesson.id}/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

        self.assertFalse(
            Lesson.objects.filter(id=self.lesson.id).exists()
        )


class CourseTestCase(APITestCase):
    """
    Тест для курса
    """

    def setUp(self) -> None:
        self.user = User.objects.create(
            name='Test', surname='Test', email='test@t.com', is_superuser=True)
        self.course = Course.objects.create(
            author=self.user, name_course='Course Name',
            description='Course Description', price=1000)
        self.module = Module.objects.create(
            author=self.user, course_id=self.course, sequence_number=1,
            name_module='Module Name', description='Module Description')
        self.lesson = Lesson.objects.create(
            name_lesson='Lesson Name', description='List Description',
            link='https://my.sky.pro/youtube.com', module_id=self.module,
            author=self.user)

    def test_create_course(self):
        """
        Тестирование создания курса
        """
        data = {
            'name_course': 'Test',
            'description': 'Test',
            'author': self.user.id,
            'price': 1000,
        }
        self.client.force_authenticate(user=self.user)

        response = self.client.post(
            '/course/create/',
            data=data
        )
        print(response.json())

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

    def test_list_course(self):
        """
        Тестирование просмотра списка курсов
        """

        response = self.client.get(
            '/'
        )
        print(response.json())

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_retrieve_course(self):
        """
        Тестирование просмотра одного курса
        """

        self.client.force_authenticate(user=self.user)

        response = self.client.get(
            f'/course/{self.course.id}/'
        )
        print(response.json())

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_update_course(self):
        """
        Тестирование изменения курса
        """

        data = {
            "name_course": "Test2",
            "description": "test",
            "author": self.user.id,
            "price": 10000,
        }

        self.client.force_authenticate(user=self.user)

        response = self.client.put(
            f'/course/update/{self.course.id}/',
            data=data
        )
        print(response.json())

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_delete_course(self):
        """
        Тестирование удаление курса
        """

        self.client.force_authenticate(user=self.user)

        response = self.client.delete(
            f'/course/delete/{self.course.id}/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )


class ModuleTestCase(APITestCase):
    """
    Тест для модуля
    """

    def setUp(self) -> None:
        self.user = User.objects.create(
            name='Test', surname='Test', email='test@t.com', is_superuser=True)
        self.course = Course.objects.create(
            author=self.user, name_course='Course Name',
            description='Course Description', price=1000)
        self.module = Module.objects.create(
            author=self.user, course_id=self.course, sequence_number=1,
            name_module='Module Name', description='Module Description')
        self.lesson = Lesson.objects.create(
            name_lesson='Lesson Name', description='List Description',
            link='https://my.sky.pro/youtube.com', module_id=self.module,
            author=self.user)

    def test_create_module(self):
        """
        Тестирование создания модуля
        """
        data = {

            "sequence_number": 1,
            "name_module": "Module Name",
            "description": "Module Description",
            "course_id": self.course.id,
            "author": self.user.id
        }
        self.client.force_authenticate(user=self.user)

        response = self.client.post(
            '/modules/create/',
            data=data
        )
        print(response.json())

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

    def test_list_module(self):
        """
        Тестирование просмотра списка модулей
        """

        response = self.client.get(
            '/modules/list/'
        )
        print(response.json())

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_retrieve_module(self):
        """
        Тестирование просмотра одного курса
        """

        self.client.force_authenticate(user=self.user)

        response = self.client.get(
            f'/modules/{self.module.id}/'
        )
        print(response.json())

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_update_module(self):
        """
        Тестирование изменения модуля
        """
        self.client.force_authenticate(user=self.user)

        data = {
            "sequence_number": 1,
            "name_module": "Test2",
            "description": "test",
            "content": "test",
            "course_id": self.course.id,
            "author": self.user.id
        }

        response = self.client.put(
            f'/modules/update/{self.module.id}/',
            data=data
        )
        print(response.json())

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_delete_module(self):
        """
        Тестирование удаление модуля
        """

        self.client.force_authenticate(user=self.user)

        response = self.client.delete(
            f'/modules/delete/{self.module.id}/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )
