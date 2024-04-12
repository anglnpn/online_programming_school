from django.db.models.signals import post_save
from django.dispatch import receiver

from payments.models import Payments
from payments.services import get_payment_status


@receiver(post_save, sender=Payments)
def create_payments_status(sender, instance, created, **kwargs):
    """
    Сигнал для записи статуса в объект оплаты
    Так как покупка происходит в тестовом формате,
    статус 'successes' устанавливаем принудительно
    """
    if created:
        instance.payment_status = 'successes'
        instance.save()

