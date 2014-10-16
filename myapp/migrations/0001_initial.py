# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Accelerometer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('max_g', models.FloatField(default=2)),
                ('value_x', models.FloatField(default=0)),
                ('value_y', models.FloatField(default=0)),
                ('value_z', models.FloatField(default=-1)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
