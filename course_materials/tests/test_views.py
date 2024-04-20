from rest_framework.test import APITestCase, APIClient
from rest_framework import status

from course_materials.models import Course, Lesson, Module
from payments.models import Payments

from users.models import User


class LessonTestCase(APITestCase):
    """
    Тестирование работы с объектом "Lesson".
    """

    def setUp(self) -> None:
        # Создание объектов для тестирования
        self.user = User.objects.create(
            name='Test', surname='Test', email='test@t.com',
            is_superuser=True, is_staff=True)
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

        self.client = APIClient()

    def test_create_lesson(self):
        """
        Тестирование создания урока.
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
            '/materials/lesson/create/',
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

    def test_create_lesson_error(self):
        """
        Тестирование ошибки создания урока.
        """
        data = {
            'name_lesson': 'Test',
            'description': 'Test',
            'link': 'https://my.sky.pro/youtube.com',
            'module_id': 'self.module.id',
            'content': 'Test content',
            'author': self.user.id
        }
        self.client.force_authenticate(user=self.user)

        response = self.client.post(
            '/materials/lesson/create/',
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )

    def test_list_lesson(self):
        """
        Тестирование просмотра списка уроков
        """
        self.client.force_authenticate(user=self.user)

        response = self.client.get(
            '/materials/lesson/'
        )

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
            f'/materials/lesson/{self.lesson.id}/'
        )

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
            f'/materials/lesson/update/{self.lesson.id}/',
            data=data
        )

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
            f'/materials/lesson/delete/{self.lesson.id}/'
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
    Тестирование работы с объектом "Course".
    """

    def setUp(self) -> None:
        self.user = User.objects.create(
            name='Test', surname='Test', email='test@t.com',
            is_superuser=True, is_staff=True)
        self.course = Course.objects.create(
            author=self.user, name_course='Course Name',
            description='Course Description', price=1000)
        self.payment = Payments.objects.create(
            payment_user=self.user, payment_course=self.course,
            payment_amount=100000, payment_status='successes',
            payment_method='transfer')
        self.module = Module.objects.create(
            author=self.user, course_id=self.course, sequence_number=1,
            name_module='Module Name', description='Module Description')
        self.lesson = Lesson.objects.create(
            name_lesson='Lesson Name', description='List Description',
            link='https://my.sky.pro/youtube.com', module_id=self.module,
            author=self.user)

        self.client = APIClient()

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
            '/materials/course/create/',
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

    def test_create_course_error(self):
        """
        Тестирование ошибки создания курса
        """
        data = {
            'description': 1,
            'price': "0",
        }
        self.client.force_authenticate(user=self.user)

        response = self.client.post(
            '/materials/course/create/',
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )

    def test_list_course(self):
        """
        Тестирование просмотра списка курсов
        """
        self.client.force_authenticate(user=self.user)

        response = self.client.get(
            '/materials/courses_list/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_course_list_purchased(self):
        """
        Тестирование просмотра списка курсов,
        которые были куплены пользователем.
        """

        self.client.force_authenticate(user=self.user)

        response = self.client.get(
            '/materials/list/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_list_users_course(self):
        """
        Тестирование просмотра списка курсов,
        которые были куплены пользователем.
        """

        self.client.force_authenticate(user=self.user)

        response = self.client.get(
            '/materials/list_user/'
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
            f'/materials/course/{self.course.id}/'
        )

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
            f'/materials/course/update/{self.course.id}/',
            data=data
        )

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
            f'/materials/course/delete/{self.course.id}/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )


class ModuleTestCase(APITestCase):
    """
    Тестирование работы с объектом "Module".
    """

    def setUp(self) -> None:
        self.user = User.objects.create(
            name='Test', surname='Test', email='test@t.com',
            is_superuser=True, is_staff=True)
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

        self.client = APIClient()

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
            '/materials/modules/create/',
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

    def test_create_module_error(self):
        """
        Тестирование ошибки создания модуля
        """
        data = {

            "sequence_number": 1,
            "name_module": "Module Name",
            "description": "Module Description",
            "course_id": "self.course.id",
            "author": "self.user.id"
        }
        self.client.force_authenticate(user=self.user)

        response = self.client.post(
            '/materials/modules/create/',
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )

    def test_list_module(self):
        """
        Тестирование просмотра списка модулей
        """
        self.client.force_authenticate(user=self.user)

        response = self.client.get(
            '/materials/modules/list/'
        )

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
            f'/materials/modules/{self.module.id}/'
        )

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
            f'/materials/modules/update/{self.module.id}/',
            data=data
        )

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
            f'/materials/modules/delete/{self.module.id}/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )
