from django.urls import path

from materials.apps import MaterialsConfig

from materials.views import (
    CourseCreateAPIView, CourseRetrieveAPIView,
    CourseUpdateAPIView, CourseDestroyAPIView,
    LessonCreateAPIView, LessonListAPIView,
    LessonRetrieveAPIView, LessonUpdateAPIView,
    LessonDestroyAPIView, ModuleCreateAPIView,
    ModuleRetrieveAPIView, ModuleUpdateAPIView,
    ModuleDestroyAPIView, ModuleListAPIView,
    CourseListAPIView, CourseListUsersAPIView,
    CourseListPurchasedAPIView)


app_name = MaterialsConfig.name

urlpatterns = [
    # курс
    path('course/create/', CourseCreateAPIView.as_view(),
         name='course'),
    path('course/<int:pk>/', CourseRetrieveAPIView.as_view(),
         name='course_get'),
    path('course/update/<int:pk>/', CourseUpdateAPIView.as_view(),
         name='course_update'),
    path('course/delete/<int:pk>/', CourseDestroyAPIView.as_view(),
         name='course_delete'),
    path('courses_list/', CourseListAPIView.as_view(), name='course_list'),
    # курс
    path('list/', CourseListPurchasedAPIView.as_view(), name='course_list'),
    path('list_user/', CourseListUsersAPIView.as_view(), name='course_list_users'),
    # модуль
    path('modules/create/', ModuleCreateAPIView.as_view(),
         name='module_create'),
    path('modules/<int:pk>/', ModuleRetrieveAPIView.as_view(),
         name='module_get'),
    path('modules/update/<int:pk>/', ModuleUpdateAPIView.as_view(),
         name='module_update'),
    path('modules/delete/<int:pk>/', ModuleDestroyAPIView.as_view(),
         name='module_delete'),
    path('modules/list/', ModuleListAPIView.as_view(),
         name='module_list'),
    # урок
    path('lesson/create/', LessonCreateAPIView.as_view(),
         name='lesson'),
    path('lesson/', LessonListAPIView.as_view(),
         name='lesson_list'),
    path('lesson/<int:pk>/', LessonRetrieveAPIView.as_view(),
         name='lesson_get'),
    path('lesson/update/<int:pk>/', LessonUpdateAPIView.as_view(),
         name='lesson_update'),
    path('lesson/delete/<int:pk>/', LessonDestroyAPIView.as_view(),
         name='lesson_delete'),

]
