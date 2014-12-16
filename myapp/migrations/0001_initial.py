# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Accelerometer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('time', models.DateTimeField(default=datetime.datetime(2014, 12, 1, 11, 6, 4, 137090), auto_now_add=True)),
                ('value_x', models.FloatField(default=0)),
                ('value_y', models.FloatField(default=0)),
                ('value_z', models.FloatField(default=-1)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Gyroscope',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('time', models.DateTimeField(default=datetime.datetime(2014, 12, 1, 11, 6, 4, 137588), auto_now_add=True)),
                ('value_x', models.FloatField(default=0)),
                ('value_y', models.FloatField(default=0)),
                ('value_z', models.FloatField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
