# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('title', models.CharField(verbose_name='Наименование', max_length=255)),
                ('caption', models.CharField(verbose_name='Описание', max_length=1000, blank=True)),
            ],
            options={
                'verbose_name': 'Альбом',
                'verbose_name_plural': 'Альбомы',
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('picture', models.ImageField(upload_to='gallery/', verbose_name='Изображение')),
                ('title', models.CharField(verbose_name='Наименование', max_length=255, blank=True)),
                ('description', models.CharField(verbose_name='Описание', max_length=1000, blank=True)),
                ('album', models.ForeignKey(verbose_name='Альбом', to='gallery.Album')),
            ],
            options={
                'verbose_name': 'Фотография',
                'verbose_name_plural': 'Фотографии',
            },
        ),
    ]
