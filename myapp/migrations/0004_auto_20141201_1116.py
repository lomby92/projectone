# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_auto_20141201_1111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accelerometer',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 1, 11, 16, 58, 731837), auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='gyroscope',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 1, 11, 16, 58, 732455), auto_now_add=True),
        ),
    ]
