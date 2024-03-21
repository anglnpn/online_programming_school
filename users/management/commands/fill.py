
from django.core.management.base import BaseCommand

from materials.models import Course
from users.models import Payments, User


class Command(BaseCommand):
    """
    Команда для создания платежа
    """

    def handle(self, *args, **kwargs):
        user = User.objects.get(id=3)
        course = Course.objects.get(id=2)
        payment = Payments.objects.create(
            payment_user=user,
            payment_course=course,
            payment_amount=150.00,
            payment_method='Перевод'
        )

        self.stdout.write(self.style.SUCCESS('Платеж сохранен'))
