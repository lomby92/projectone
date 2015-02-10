# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0021_auto_20141204_0923'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attitude',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('time', models.DateTimeField(default=datetime.datetime(2014, 12, 4, 11, 7, 14, 364959), auto_now_add=True)),
                ('roll', models.FloatField(default=0)),
                ('pitch', models.FloatField(default=0)),
                ('yaw', models.FloatField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='accelerometer',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 4, 11, 7, 14, 363626), auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='gyroscope',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 4, 11, 7, 14, 364132), auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='magnetometer',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 4, 11, 7, 14, 364546), auto_now_add=True),
        ),
    ]
