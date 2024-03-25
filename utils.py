from elasticsearch import Elasticsearch

from config import settings


def __str__(self):
    rubrics = self.rubrics
    for rubric in rubrics:
        rubric_theme = rubric['theme']
    return f"Название: '{rubric_theme}', лекция создана: {self.created_date})"
