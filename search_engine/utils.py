from django_elasticsearch_dsl.registries import registry
from django_elasticsearch_dsl import Document

from .models import Text


@registry.register_document
class TextDocument(Document):
    class Index:
        # Имя elastic-индекса
        name = 'text1'
        # Настройки elastic
        settings = {'number_of_shards': 1,
                    'number_of_replicas': 0}

    class Django:
        # Связанная с elastic модель Django DRF
        model = Text

        # Поля модели Django, которые будут связаны и переданы в elastic
        fields = [
            'rubrics',
            'theme',
            'text',
            'created_date',
        ]

