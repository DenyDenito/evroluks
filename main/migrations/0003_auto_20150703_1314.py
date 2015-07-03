# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20150626_1523'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slide',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Image', models.ImageField(upload_to='slides/')),
                ('header', models.CharField(verbose_name='Заголовок', max_length=120)),
                ('caption', models.CharField(blank=True, verbose_name='Описание', max_length=250)),
            ],
            options={
                'verbose_name': 'слайд',
                'verbose_name_plural': 'слайды',
            },
        ),
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name': 'заявка', 'verbose_name_plural': 'заявки'},
        ),
    ]
