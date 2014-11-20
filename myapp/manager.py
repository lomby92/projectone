import time

from connections import MAVlinkConnection
from models import Accelerometer


class Manager(object):

    __manager_instance = None

    @classmethod
    def get_instance(cls):
        if cls.__manager_instance is None:
            cls.__manager_instance = object.__new__(Manager)
        return cls.__manager_instance

    def start_mav(self):
        #-------------------- define variables --------------------
        self.mav_connection = None
        self.mav_is_to_disconnect = False
        #-------------------- try to connect --------------------
        try:
            self.mav_connection = MAVlinkConnection('/dev/ttyACM0', 115200)
            #connected
            return 1
        except:
            self.mav_connection = None
            #unable to connect
            return 0

    # start_test_bench is incomplete
    def start_test_bench(self):
        #-------------------- define variables --------------------
        self.test_bench_connection = None
        self.test_bench_is_to_disconnect = False
        #-------------------- try to connect --------------------
        try:
            #self.test_bench_connection = TestBenchConnection('', 0)
            #connected
            return 1
        except:
            self.test_bench_connection = None
            #unable to connect
            return 0

    def run_mav(self):
        while not self.mav_is_to_disconnect:
            #read accelerometer:
            x, y, z = self.mav_connection.read_accelerometer()
            Accelerometer.objects.create(value_x=x, value_y=y, value_z=z).save()
            #-----to do: add all sensors-----
            time.sleep(self.mav_connection.get_freq())
        self.stop_mav()

    def run_test_bench(self):
        pass

    def stop_mav(self):
        self.mav_connection.close()

    def stop_test_bench(self):
        pass
        self.test_bench_connection.close()