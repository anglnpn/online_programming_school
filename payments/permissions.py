from rest_framework.permissions import BasePermission


class IsModerPayment(BasePermission):
    """
    Проверка на модератора оплат
    """

    def has_permission(self, request, view):
        if request.user.is_staff:
            return request.user.groups.filter(
                name='moderator_payment').exists() \
                or request.user.is_superuser
        else:
            return False


class IsContributor(BasePermission):
    """
    Проверка, что оплата принадлежит пользователю
    """

    def has_object_permission(self, request, view, obj):
        return request.user == obj.payment_user
