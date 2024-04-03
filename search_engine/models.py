from django.db import models

from config.settings import NAME_CHOICES


class Text(models.Model):
    id = models.AutoField(primary_key=True)
    rubrics = models.CharField(max_length=100, verbose_name='рубрики', choices=NAME_CHOICES)
    theme = models.CharField(max_length=100, verbose_name='темы')
    text = models.TextField(verbose_name='текст')
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Тема: {self.theme}, дата создания:{self.created_date})"

