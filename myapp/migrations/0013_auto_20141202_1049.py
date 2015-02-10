# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0012_auto_20141202_1049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accelerometer',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 2, 10, 49, 43, 95541), auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='gyroscope',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 2, 10, 49, 43, 96167), auto_now_add=True),
        ),
    ]
