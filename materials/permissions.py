from rest_framework.permissions import BasePermission

from materials.models import Course, Module, Lesson
from payments.models import Payments


class IsModer(BasePermission):
    """
    Проверка на модератора
    """

    def has_permission(self, request, view):
        if request.user.is_staff:
            return request.user.groups.filter(name='moderator').exists()
        else:
            return False


class IsUserPaymentStatus(BasePermission):
    """
    Проверка, что пользователь оплатил курс или модуль.
    """

    def has_object_permission(self, request, view, obj):
        if isinstance(obj, Course):
            course_id = obj.id
            print(course_id)
            user_id = request.user.id
            print(user_id)
            payment = Payments.objects.filter(
                payment_course=course_id,
                payment_user=user_id,
                payment_status='successes'
            )
            print(payment)
        elif isinstance(obj, Module):
            module = obj
            course_id = module.course_id.id
            user_id = request.user.id
            payment = Payments.objects.filter(
                payment_course=course_id,
                payment_user=user_id,
                payment_status='successes'
            )

        elif isinstance(obj, Lesson):
            lesson = obj
            course_id = lesson.module_id.course_id.id
            user_id = request.user.id
            payment = Payments.objects.filter(
                payment_course=course_id,
                payment_user=user_id,
                payment_status='successes'
            )

        else:
            return False

        return bool(payment)
