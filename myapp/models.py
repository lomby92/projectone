from django.db import models

from datetime import datetime


class Accelerometer(models.Model):

    time = models.DateTimeField(auto_now_add=True, default=datetime.now())
    value_x = models.FloatField(default=0)
    value_y = models.FloatField(default=0)
    value_z = models.FloatField(default=-1)

    @staticmethod
    def last_value():
        last_record = Accelerometer.objects.last()
        last_value = [float(last_record.time.strftime('%Y%m%d%H%M%S%f')[:-3]),
                      last_record.value_x,
                      last_record.value_y,
                      last_record.value_z]
        return last_value


class Gyroscope(models.Model):

    time = models.DateTimeField(auto_now_add=True, default=datetime.now())
    value_x = models.FloatField(default=0)
    value_y = models.FloatField(default=0)
    value_z = models.FloatField(default=0)

    @staticmethod
    def last_value():
        last_record = Gyroscope.objects.last()
        last_value = [float(last_record.time.strftime('%Y%m%d%H%M%S%f')[:-3]),
                      last_record.value_x,
                      last_record.value_y,
                      last_record.value_z]
        return last_value


class Magnetometer(models.Model):


    time = models.DateTimeField(auto_now_add=True, default=datetime.now())
    value_x = models.FloatField(default=0)
    value_y = models.FloatField(default=0)
    value_z = models.FloatField(default=0)

    @staticmethod
    def last_value():
        last_record = Magnetometer.objects.last()
        last_value = [float(last_record.time.strftime('%Y%m%d%H%M%S%f')[:-3]),
                      last_record.value_x,
                      last_record.value_y,
                      last_record.value_z]
        return last_value


class Attitude(models.Model):

    time = models.DateTimeField(auto_now_add=True, default=datetime.now())
    roll = models.FloatField(default=0)
    pitch = models.FloatField(default=0)
    yaw = models.FloatField(default=0)

    @staticmethod
    def last_value():
        last_record = Magnetometer.objects.last()
        last_value = [float(last_record.time.strftime('%Y%m%d%H%M%S%f')[:-3]),
                      last_record.roll,
                      last_record.pitch,
                      last_record.yaw]
        return last_value