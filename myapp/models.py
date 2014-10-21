from django.db import models

from datetime import datetime


class Accelerometer(models.Model):

    MAX_VALUE_OF_SENSOR = 32767.0

    max_g = models.FloatField(default=2)
    time = models.DateTimeField(auto_now_add=True, default=datetime.now)
    value_x = models.FloatField(default=0)
    value_y = models.FloatField(default=0)
    value_z = models.FloatField(default=-1)