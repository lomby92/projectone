import djqscsv

from models import Accelerometer


def create_accelerometer_value():
    test = Accelerometer.objects.create(max_g=2, value_x=1.1,
                                        value_y=1.2, value_z=1.3)
    test.save()
    return Accelerometer.objects.all()


def save_csv():
    try:
        obj = Accelerometer.objects.all()
        filecsv = open("accelerometer_csv.txt", "w")
        djqscsv.write_csv(obj, filecsv)
    except:
        pass