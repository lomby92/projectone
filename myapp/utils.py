import djqscsv
import random

from models import Accelerometer


def create_accelerometer_value():
    max_g = Accelerometer.objects.all()[1].max_g
    max_sensor = Accelerometer.MAX_VALUE_OF_SENSOR
    x = max_g*(random.randint(-max_sensor, max_sensor))/max_sensor
    y = max_g*(random.randint(-max_sensor, max_sensor))/max_sensor
    z = max_g*(random.randint(-max_sensor, max_sensor))/max_sensor
    test = Accelerometer.objects.create(max_g=2, value_x=x,
                                        value_y=y, value_z=z)
    test.save()


def save_csv():
    try:
        obj = Accelerometer.objects.all()
        #last_set = Accelerometer.objects.order_by('-id')[1]
        filecsv = open("accelerometer_csv.txt", "w")
        djqscsv.write_csv(obj, filecsv)
    except:
        pass