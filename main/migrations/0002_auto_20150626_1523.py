# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date_execution',
            field=models.DateTimeField(verbose_name='Удобное время исполнения'),
        ),
    ]
