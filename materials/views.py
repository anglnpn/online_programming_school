from datetime import datetime
from rest_framework import generics
from materials.models import Course, Lesson, Module
from materials.paginators import MaterialsPagination
from materials.permissions import IsModer, IsUserPaymentStatus
from materials.serializers import (CourseSerializer,
                                   LessonSerializer,
                                   ModuleSerializer,
                                   CourseListSerializer)

from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.renderers import TemplateHTMLRenderer

from rest_framework.response import Response

from materials.tasks import send_moderator_email

from rest_framework.views import APIView

import requests
from django.shortcuts import render, get_object_or_404, redirect


class CourseCreateAPIView(generics.CreateAPIView):
    """
    Создание курса
    """
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    permission_classes = [IsAuthenticated, IsModer]
    # permission_classes = [AllowAny]
    # renderer_classes = [TemplateHTMLRenderer]
    # template_name = 'materials/course_create.html'

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    # def get(self, request):
    #     serializer = CourseSerializer()
    #
    #     return Response({'serializer': serializer})
    #
    # def post(self, request):
    #     serializer = CourseSerializer(data=request.data)
    #     if not serializer.is_valid():
    #         return Response({'serializer': serializer})
    #     serializer.save()
    #     return redirect(reverse('materials:list'))


class CourseListAPIView(generics.ListAPIView):
    """
    Вывод списка курсов
    """
    queryset = Course.objects.all()
    serializer_class = CourseListSerializer
    permission_classes = [IsAuthenticated]
    # permission_classes = [AllowAny]
    pagination_class = MaterialsPagination
    # renderer_classes = [TemplateHTMLRenderer]
    # template_name = 'materials/index.html'

    def get(self, request):
        queryset = Course.objects.all()
        paginated_queryset = self.paginate_queryset(queryset)
        serializer = CourseListSerializer(paginated_queryset, many=True)
        return self.get_paginated_response(serializer.data)
        # return Response({'courses': queryset})


# def index(request):
#     course_list_view = CourseListAPIView()
#     serializer_data = course_list_view.get_serializer(course_list_view.get_queryset(), many=True).data
#     return Response({'serializer_data': serializer_data})


class CourseRetrieveAPIView(generics.RetrieveAPIView):
    """
    Просмотр одного курса
    """
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    permission_classes = [IsAuthenticated, IsModer | IsUserPaymentStatus]
    # permission_classes = [AllowAny]


class CourseUpdateAPIView(generics.UpdateAPIView):
    """
    Изменение курса
    """
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    permission_classes = [IsAuthenticated, IsModer]
    # permission_classes = [AllowAny]
    # renderer_classes = [TemplateHTMLRenderer]
    # template_name = 'materials/course_update.html'
    #
    # def get(self, request, pk):
    #     course = get_object_or_404(Course, pk=pk)
    #     serializer = CourseSerializer(course)
    #     return Response({'serializer': serializer, 'course': course})


class ModuleCreateAPIView(generics.CreateAPIView):
    """
    Создание модуля курса
    """
    serializer_class = ModuleSerializer
    queryset = Module.objects.all()
    permission_classes = [IsAuthenticated, IsModer]
    # permission_classes = [AllowAny]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class ModuleListAPIView(generics.ListAPIView):
    """
    Вывод списка модулей курса
    """
    serializer_class = ModuleSerializer
    queryset = Module.objects.all()
    permission_classes = [IsAuthenticated, IsModer | IsUserPaymentStatus]
    # permission_classes = [AllowAny]


class ModuleRetrieveAPIView(generics.RetrieveAPIView):
    """
    Просмотр одного модуля курса
    """
    serializer_class = ModuleSerializer
    queryset = Module.objects.all()
    permission_classes = [IsAuthenticated, IsModer | IsUserPaymentStatus]
    # permission_classes = [AllowAny]


class ModuleUpdateAPIView(generics.UpdateAPIView):
    """
    Изменение модуля курса
    """
    serializer_class = ModuleSerializer
    queryset = Module.objects.all()

    permission_classes = [IsAuthenticated, IsModer]
    # permission_classes = [AllowAny]

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

        module_id = serializer.data['id']

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
    # permission_classes = [AllowAny]


class CourseDestroyAPIView(generics.DestroyAPIView):
    """
    Удаление курса
    """
    queryset = Course.objects.all()
    permission_classes = [IsAuthenticated, IsModer]
    # permission_classes = [AllowAny]


class LessonCreateAPIView(generics.CreateAPIView):
    """
    Cоздание урока
    """
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()

    permission_classes = [IsAuthenticated, IsModer]
    # permission_classes = [AllowAny]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class LessonListAPIView(generics.ListAPIView):
    """
    Просмотр списка уроков
    """
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsModer | IsUserPaymentStatus]
    permission_classes = [AllowAny]
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
    # permission_classes = [AllowAny]


class LessonUpdateAPIView(generics.UpdateAPIView):
    """
    Изменение урока
    """
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsModer]
    # permission_classes = [AllowAny]

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

        # получаем объект курса
        course_obj = module_obj.course_id
        course_id = course_obj.id

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
    # permission_classes = [AllowAny]
