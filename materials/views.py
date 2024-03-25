from datetime import datetime
from rest_framework import generics
from materials.models import Course, Lesson, Module
from materials.paginators import MaterialsPagination
from materials.permissions import IsModer, IsUserPaymentStatus
from materials.serializers import (CourseSerializer,
                                   LessonSerializer,
                                   ModuleSerializer,
                                   CourseListSerializer)

from rest_framework.permissions import IsAuthenticated

from materials.tasks import send_moderator_email


class CourseCreateAPIView(generics.CreateAPIView):
    """
    Создание курса
    """
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    permission_classes = [IsAuthenticated, IsModer]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CourseListAPIView(generics.ListAPIView):
    """
    Вывод списка курсов
    """
    queryset = Course.objects.all()
    serializer_class = CourseListSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = MaterialsPagination

    def get(self, request):
        queryset = Course.objects.all()
        paginated_queryset = self.paginate_queryset(queryset)
        serializer = CourseListSerializer(paginated_queryset, many=True)
        return self.get_paginated_response(serializer.data)


class CourseRetrieveAPIView(generics.RetrieveAPIView):
    """
    Просмотр одного курса
    """
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    permission_classes = [IsAuthenticated, IsModer | IsUserPaymentStatus]


class CourseUpdateAPIView(generics.UpdateAPIView):
    """
    Изменение курса
    """
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    permission_classes = [IsAuthenticated, IsModer]


class ModuleCreateAPIView(generics.CreateAPIView):
    """
    Создание модуля курса
    """
    serializer_class = ModuleSerializer
    queryset = Module.objects.all()
    permission_classes = [IsAuthenticated, IsModer]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class ModuleListAPIView(generics.ListAPIView):
    """
    Вывод списка модулей курса
    """
    serializer_class = ModuleSerializer
    queryset = Module.objects.all()
    permission_classes = [IsAuthenticated, IsModer | IsUserPaymentStatus]


class ModuleRetrieveAPIView(generics.RetrieveAPIView):
    """
    Просмотр одного модуля курса
    """
    serializer_class = ModuleSerializer
    queryset = Module.objects.all()
    permission_classes = [IsAuthenticated, IsModer | IsUserPaymentStatus]


class ModuleUpdateAPIView(generics.UpdateAPIView):
    """
    Изменение модуля курса
    """
    serializer_class = ModuleSerializer
    queryset = Module.objects.all()

    permission_classes = [IsAuthenticated, IsModer]

    def perform_update(self, serializer):
        """
        Получает id курса из данных урока.
        Вызывает функцию send_moderator_email.
        """
        serializer.save()
        data = self.request.data

        print(self.request)
        # получаем id курса из данных
        course_id = data.get('course_id')
        module_id = data.get('id')

        # получаем объект курса
        course_obj = Course.objects.get(id=course_id)

        # обновляем дату изменения курса
        course_obj.update_date = datetime.utcnow()
        course_obj.save()

        # Получаем объект модуля
        module_obj = Module.objects.get(id=module_id)

        # обновляем дату изменения module
        module_obj.update_date = datetime.utcnow()
        module_obj.save()

        # вызываем отложенную задачу для отправки письма
        send_moderator_email.delay(course_id)


class ModuleDestroyAPIView(generics.DestroyAPIView):
    """
    Удаление модуля курса
    """
    queryset = Module.objects.all()
    permission_classes = [IsAuthenticated, IsModer]


class CourseDestroyAPIView(generics.DestroyAPIView):
    """
    Удаление курса
    """
    queryset = Course.objects.all()
    permission_classes = [IsAuthenticated, IsModer]


class LessonCreateAPIView(generics.CreateAPIView):
    """
    Cоздание урока
    """
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()

    permission_classes = [IsAuthenticated, IsModer]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class LessonListAPIView(generics.ListAPIView):
    """
    Просмотр списка уроков
    """
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsModer | IsUserPaymentStatus]
    pagination_class = MaterialsPagination

    # def get(self, request):
    #     queryset = Lesson.objects.all()
    #     paginated_queryset = self.paginate_queryset(queryset)
    #     serializer = LessonSerializer(paginated_queryset, many=True)
    #     return self.get_paginated_response(serializer.data)


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    """
    Просмотр одного урока
    """
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsModer | IsUserPaymentStatus]


class LessonUpdateAPIView(generics.UpdateAPIView):
    """
    Изменение урока
    """
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsModer]

    def perform_update(self, serializer):
        """
        Получает id модуля из данных урока.
        Вызывает функцию send_moderator_email.
        """
        serializer.save()
        data = self.request.data
        # получаем id курса из данных
        module_id = data.get('module_id')

        # получаем объект module
        module_obj = Module.objects.get(id=module_id)
        course_id = module_obj.course_id

        # получаем объект курса
        course_obj = Course.objects.get(id=course_id)

        # обновляем дату изменения module
        module_obj.update_date = datetime.utcnow()
        module_obj.save()

        # обновляем дату изменения курса
        course_obj.update_date = datetime.utcnow()
        course_obj.save()

        # вызываем отложенную задачу для отправки письма
        send_moderator_email.delay(course_id)


class LessonDestroyAPIView(generics.DestroyAPIView):
    """
    Удаление уроков
    """
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsModer]
