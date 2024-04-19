from django.db.models.signals import post_save
from django.dispatch import receiver

from search_engine.models import Text
from search_engine.utils import TextDocument

import logging

logging.basicConfig(level=logging.INFO)


@receiver(post_save, sender=Text)
def create_elastic_text(sender, instance, created, **kwargs):
    """
    Сигнал, который создает и сохраняет индекс, если он еще не был создан.
    Обрабатывает запрос, если индекс с таким именем уже
    существует при создании экземпляра класса Text(models).
    """

    logging.info("Сигнал успешно сработал")

    # Проверка создания экземпляра класса Text
    if created:
        # Если индекс уже существует
        if TextDocument.Index.name:
            logging.info(f"Индекс '{TextDocument.Index.name}' уже существует")

        # Если индекс еще не создан
        else:
            TextDocument.init()
            logging.info(
                f"Индекс '{TextDocument.Index.name}' "
                f"создан для '{instance}'")
    else:
        logging.info(
            "Экземпляр класса Text был удален или создан с ошибкой. "
            "Попробуйте еще раз.")
