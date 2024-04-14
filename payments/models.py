from django.db import models

from course_materials.models import Course
from users.models import User

from config.utils import NULLABLE


class Payments(models.Model):
    """
    Модель для создания платежа пользователя
    """
    payment_user = models.ForeignKey(
        User, on_delete=models.CASCADE,
        verbose_name='пользователь')
    payment_date = models.DateTimeField(
        auto_now=True, editable=False,
        verbose_name='дата платежа')
    payment_course = models.ForeignKey(
        Course, on_delete=models.CASCADE,
        null=True, blank=True,
        verbose_name='курс оплаченный')
    payment_amount = models.IntegerField(
        verbose_name='сумма оплаты', **NULLABLE)
    payment_method = models.CharField(
        max_length=50, choices=[('cash', 'Наличные'),
                                ('transfer', 'Перевод')])
    payment_session_id = models.CharField(
        max_length=1000, blank=True, null=True,
        verbose_name='идентификатор сессии платежа')
    payment_status = models.CharField(
        max_length=50,
        choices=[('successes', 'Успешно'), ('failed', 'Неуспешно')],
        **NULLABLE)

    def __str__(self):
        return f'{self.payment_user} {self.payment_date}'

    class Meta:
        verbose_name = 'платеж'
        verbose_name_plural = 'платежи'


class Subscribe(models.Model):
    """
    Модель для подписки на курс
    """
    user = models.ForeignKey(
        User, on_delete=models.CASCADE,
        verbose_name='пользователь')
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE,
        verbose_name='курс')

    class Meta:
        verbose_name = 'подписка'
        verbose_name_plural = 'подписки'
