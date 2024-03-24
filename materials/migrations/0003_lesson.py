# Generated by Django 4.2.10 on 2024-03-21 16:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('materials', '0002_module'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_lesson', models.CharField(max_length=50, verbose_name='название урока')),
                ('image', models.ImageField(blank=True, null=True, upload_to='static/', verbose_name='картинка урока')),
                ('description', models.TextField(verbose_name='описание урока')),
                ('content', models.TextField(verbose_name='содержание урока')),
                ('link', models.CharField(max_length=50, verbose_name='ссылка на видео')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='автор')),
                ('module_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='materials.module', verbose_name='модуль урока')),
            ],
            options={
                'verbose_name': 'урок',
                'verbose_name_plural': 'уроки',
            },
        ),
    ]
