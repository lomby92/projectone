from django.db import models

from datetime import datetime
import time


class Accelerometer(models.Model):

    time = models.DateTimeField(auto_now_add=True, default=datetime.now())
    value_x = models.FloatField(default=0)
    value_y = models.FloatField(default=0)
    value_z = models.FloatField(default=-1)

    @staticmethod
    def last_value():
        qs = Accelerometer.objects.order_by('-id')
        last_items = qs.all()[0]
        timetuple = last_items.time.timetuple()
        timestamp = time.mktime(timetuple)
        last_value = [timestamp*1000,
                      last_items.value_x,
                      last_items.value_y,
                      last_items.value_z]
        return last_value