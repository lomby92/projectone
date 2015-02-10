# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0019_auto_20141202_1120'),
    ]

    operations = [
        migrations.CreateModel(
            name='Magnetometer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('time', models.DateTimeField(default=datetime.datetime(2014, 12, 4, 9, 22, 59, 64639), auto_now_add=True)),
                ('value_x', models.FloatField(default=0)),
                ('value_y', models.FloatField(default=0)),
                ('value_z', models.FloatField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='accelerometer',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 4, 9, 22, 59, 63551), auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='gyroscope',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 4, 9, 22, 59, 64119), auto_now_add=True),
        ),
    ]
