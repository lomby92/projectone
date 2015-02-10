# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0020_auto_20141204_0922'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accelerometer',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 4, 9, 23, 18, 296126), auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='gyroscope',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 4, 9, 23, 18, 296613), auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='magnetometer',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 4, 9, 23, 18, 297034), auto_now_add=True),
        ),
    ]
