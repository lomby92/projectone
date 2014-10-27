import time

from utils import UtilsManager
from connections import MAVlinkConnection
from models import Accelerometer


class Manager():

    def __init__(self):
        self.mav_connection = None
        while self.mav_connection is None:
            try:
                self.mav_connection = MAVlinkConnection('/dev/ttyACM0', 115200)
            except:
                self.mav_connection = None
        self.util = UtilsManager()
        self.run_manager()

    def run_manager(self):
        while True:
            if self.util.is_mavlink_to_disconnect():
                self.mav_connection.close()
            #read_accelerometer try to capture data
            x, y, z = self.mav_connection.read_accelerometer()
            acc_value = Accelerometer.objects.create(max_g=2, value_x=x,
                                                     value_y=y, value_z=z)
            acc_value.save()
            time.sleep(0.2)
