# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('image', models.ImageField(upload_to='services/', verbose_name='Изображение')),
                ('title', models.CharField(verbose_name='Наименование', max_length=120)),
                ('description', models.TextField(verbose_name='Описание')),
                ('short_description', models.TextField(verbose_name='Краткое описание')),
            ],
            options={
                'verbose_name': 'Услуга',
                'verbose_name_plural': 'Услуги',
            },
        ),
    ]
