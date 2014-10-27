import djqscsv

from connections import MAVlinkConnection
from models import Accelerometer


class UtilsManager():

    def __init__(self):
        self.mavlink_to_disconnect = False

    def is_mavlink_to_disconnect(self):
        return self.mavlink_to_disconnect

    def update_and_save_accelerometer_data():
        #to-do recognize max-g
        value = Accelerometer.objects.create(max_g=2, value_x=x,
                                             value_y=y, value_z=z)
        value.save()

    def save_csv(self):
        try:
            obj = Accelerometer.objects.all()
            #last_set = Accelerometer.objects.order_by('-id')[1]
            filecsv = open("accelerometer_csv.txt", "w")
            djqscsv.write_csv(obj, filecsv)
        except:
            pass