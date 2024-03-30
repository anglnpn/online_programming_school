from rest_framework.test import APITestCase

from materials.models import Course, Module
from materials.serializers import (
    LessonSerializer, ModuleSerializer,
    CourseSerializer)
from users.models import User


class LessonSerializerTest(APITestCase):
    """
    Тестирование сериализации модели урока.
    """

    def setUp(self):
        self.user = User.objects.create(
            name='Test', surname='Test',
            email='test@t.com', is_superuser=True)
        self.course = Course.objects.create(
            author=self.user, name_course='Course Name',
            description='Course Description', price=1000)
        self.module = Module.objects.create(
            author=self.user, course_id=self.course,
            sequence_number=1, name_module='Module Name',
            description='Module Description')

    def test_valid_data(self):
        """
        Проверяет, что сериализатор
        корректно валидирует корректные данные.
        """

        lesson_data = {
            "name_lesson": "Lesson Name",
            "description": "List Description",
            "link": "https://youtube.com",
            "content": "List content",
            "module_id": self.module.id,
            "author": self.user.id
        }

        serializer = LessonSerializer(data=lesson_data)
        self.assertTrue(serializer.is_valid())

    def test_invalid_data(self):
        """
        Проверяет, что сериализатор
        корректно валидирует некорректные данные.
        """

        lesson_data = {
            "name_lesson": "",
            "description": "",
            "link": "https://youtube.com",
            "content": "List content",
            "module_id": self.module.id,
            "author": self.user.id
        }

        serializer = LessonSerializer(data=lesson_data)
        self.assertFalse(serializer.is_valid())


class ModuleSerializerTest(APITestCase):
    """
    Тестирование сериализации модели модуля.
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

        module_data = {
            "sequence_number": 1,
            "name_module": "Module Name",
            "description": "Module Description",
            "course_id": self.course.id,
            "author": self.user.id
        }

        serializer = ModuleSerializer(data=module_data)
        self.assertTrue(serializer.is_valid())

    def test_invalid_data(self):
        """
        Проверяет, что сериализатор
        корректно валидирует некорректные данные.
        """

        module_data = {
            "sequence_number": 1,
            "name_module": "",
            "description": "Test",
            "course_id": self.course.id,
            "author": self.user.id
        }

        serializer = ModuleSerializer(data=module_data)
        self.assertFalse(serializer.is_valid())


class CourseSerializerTest(APITestCase):
    """
    Тестирование сериализации модели курса.
    """

    def setUp(self):
        self.user = User.objects.create(
            name='Test', surname='Test',
            email='test@t.com', is_superuser=True)

    def test_valid_data(self):
        """
        Проверяет, что сериализатор
        корректно валидирует корректные данные.
        """

        course_data = {
            "name_course": "Course Name",
            "description": "Course Description",
            "author": self.user.id
        }

        serializer = CourseSerializer(data=course_data)
        self.assertTrue(serializer.is_valid())

    def test_invalid_data(self):
        """
        Проверяет, что сериализатор
        корректно валидирует некорректные данные.
        """

        course_data = {
            "name_course": "",
            "description": "Course Description",
            "author": self.user.id
        }

        serializer = CourseSerializer(data=course_data)
        self.assertFalse(serializer.is_valid())
