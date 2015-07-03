# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Promo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('image', models.ImageField(upload_to='promos/', verbose_name='Изображение')),
                ('title', models.CharField(verbose_name='Наименование', max_length=120)),
                ('description', models.TextField(verbose_name='Описание')),
                ('short_description', models.TextField(verbose_name='Краткое описание')),
                ('date', models.DateTimeField(verbose_name='Дата публикации', default=datetime.datetime.now)),
            ],
            options={
                'verbose_name': 'Акция',
                'ordering': ('-date',),
                'verbose_name_plural': 'Акции',
            },
        ),
    ]
