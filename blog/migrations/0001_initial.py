# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogEntry',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('title', models.CharField(verbose_name='Заголовок', max_length=255)),
                ('body', models.TextField(verbose_name='Содержание')),
                ('slug', models.SlugField(verbose_name='Наименование ссылки', unique=True)),
                ('date', models.DateTimeField(verbose_name='Дата публикации', default=datetime.datetime.now)),
                ('picture', models.ImageField(upload_to='blog/', verbose_name='Изображение')),
            ],
            options={
                'verbose_name_plural': 'Записи',
                'ordering': ('-date',),
                'verbose_name': 'Запись',
            },
        ),
    ]
