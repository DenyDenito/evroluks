# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(verbose_name='Имя', max_length=255)),
                ('phone', models.CharField(verbose_name='Телефон', max_length=255)),
                ('message', models.TextField(verbose_name='Что нуждается в чистке')),
                ('email', models.EmailField(verbose_name='E-mail', max_length=254)),
                ('address', models.CharField(verbose_name='Адрес', max_length=255)),
                ('date_execution', models.DateTimeField(verbose_name='Удобное время')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Дата заявки')),
            ],
            options={
                'verbose_name_plural': 'Заявки',
                'verbose_name': 'Заявка',
            },
        ),
    ]
