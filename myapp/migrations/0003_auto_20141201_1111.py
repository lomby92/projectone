# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20141201_1109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accelerometer',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 1, 11, 11, 35, 916931), auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='gyroscope',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 1, 11, 11, 35, 917417), auto_now_add=True),
        ),
    ]
