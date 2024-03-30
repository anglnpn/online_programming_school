from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    """
    Команда для создания пользователя
    """
    def handle(self, *args, **options):
        user = User.objects.create(
            email='admin11@sky.pro',
            name='admin',
            surname='admin',
            is_staff=True,
            is_superuser=True

        )

        user.set_password('admin123456')
        user.save()
# модератор контента
# user@sky.pro
# user
# модератор оплат
# user2@sky.pro
# user

# просто юзер
# user3@sky.pro
#  user