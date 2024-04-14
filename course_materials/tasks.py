from datetime import datetime, timedelta

from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail

from course_materials.models import Course
from payments.models import Subscribe
from users.models import User

import logging

logging.basicConfig(level=logging.DEBUG)


@shared_task
def send_moderator_email(course_id):
    """
    Отправляет сообщения пользователям, которые
    подписаны на обновления материала курса.
    """
    email_list = []
    subscribe = Subscribe.objects.filter(course_id=course_id).all()
    course = Course.objects.filter(
        id=course_id, update_date__lt=datetime.utcnow() - timedelta(hours=4))

    if course:
        for sub in subscribe:
            user = User.objects.get(id=sub.user_id)
            email_list.append(user.email)

        try:
            send_mail(
                subject='Обновления курса',
                message='В курсе произошли обновления материала',
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=email_list
            )
            logging.info("Рассылка отправлена")
        except Exception as e:
            logging.warning(str(e), "Ошибка при отправке")
    else:
        logging.warning("Курс был недавно обновлен")

    return "success"