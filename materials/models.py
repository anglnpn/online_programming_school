from django.db import models

from config.utils import NULLABLE
from users.models import User


class Course(models.Model):
    """
    Модель для создания курса.
    Курс содержит модули.
    Модули содержат уроки.
    """
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='автор')
    name_course = models.CharField(max_length=50, verbose_name='название курса')
    image = models.ImageField(upload_to='media/', verbose_name='картинка курса', **NULLABLE)
    description = models.CharField(max_length=500, verbose_name='описание курса')
    price = models.IntegerField(verbose_name='цена курса', **NULLABLE)
    update_date = models.DateTimeField(auto_now=True, verbose_name='дата изменения', **NULLABLE)

    def __str__(self):
        return f'{self.name_course}'

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'


class Module(models.Model):
    """
    Модель для создания модуля.
    """
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='автор')
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='курс модуля')
    sequence_number = models.PositiveSmallIntegerField(verbose_name='порядковый номер')
    name_module = models.CharField(max_length=50, verbose_name='название модуля')
    description = models.TextField(verbose_name='описание модуля')
    image = models.ImageField(upload_to='static/', verbose_name='картинка модуля', **NULLABLE)
    update_date = models.DateTimeField(auto_now=True, verbose_name='дата изменения', **NULLABLE)


class Lesson(models.Model):
    """
    Модель для создания урока
    """
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='автор')
    module_id = models.ForeignKey(Module, on_delete=models.CASCADE, verbose_name='модуль урока')
    name_lesson = models.CharField(max_length=50, verbose_name='название урока')
    image = models.ImageField(upload_to='static/', verbose_name='картинка урока', **NULLABLE)
    description = models.TextField(verbose_name='описание урока')
    content = models.TextField(verbose_name='содержание урока')
    link = models.CharField(max_length=50, verbose_name='ссылка на видео')

    def __str__(self):
        return f'{self.name_lesson}'

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'
