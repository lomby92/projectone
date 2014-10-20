from django.db import models


class Accelerometer(models.Model):

    MAX_VALUE_OF_SENSOR = 32767.0

    max_g = models.FloatField(default=2)
    value_x = models.FloatField(default=0)
    value_y = models.FloatField(default=0)
    value_z = models.FloatField(default=-1)