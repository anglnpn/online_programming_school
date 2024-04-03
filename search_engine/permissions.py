from rest_framework.permissions import BasePermission


class IsTextModer(BasePermission):
    """
    Проверка на модератора текста
    """

    def has_permission(self, request, view):
        if request.user.is_staff:
            return request.user.groups.filter(name='text_moderator').exists() \
                or request.user.is_superuser
        else:
            return False
