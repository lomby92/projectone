from connections import MAVlinkConnection
from models import Accelerometer, Gyroscope, Magnetometer, Attitude
from threading import Lock
import time


class Manager(object):

    __manager_instance = None

    @classmethod
    def get_instance(cls):
        if cls.__manager_instance is None:
            cls.__manager_instance = object.__new__(Manager)
            cls.__manager_instance.__init__()
        return cls.__manager_instance

    def __init__(self):
        #define variables for connections
        self.mav_connection = None
        self.test_bench_connection = None
        self.mav_is_to_disconnect = None
        self.test_bench_is_to_disconnect = None
        #define lock for external access to fast_access_data
        self.lock = Lock()
        #define dictionary for last data to stream
        self.fast_access_data = {}
        #--------------------------testing---------------------------
        print "Ho finito la fase di init del Manager"

    def start_mav(self):
        #-------------------- try to connect --------------------
        try:
            #setting device and baudrate (in accordance of
            # http://copter.ardupilot.com/wiki/common-using-the-3dr-radio-for-telemetry-with-apm-and-px4/)
            self.mav_connection = MAVlinkConnection('/dev/ttyACM0', 57600)
            if self.mav_connection.is_connected():
                return True
            else:
                self.mav_connection = None
                return False
        except:
            self.mav_connection = None
            #unable to connect
            return False

    # start_test_bench is incomplete
    def start_test_bench(self):
        #-------------------- define variables --------------------
        self.test_bench_connection = None
        self.test_bench_is_to_disconnect = False
        #-------------------- try to connect --------------------
        try:
            #self.test_bench_connection = TestBenchConnection('', 0)
            #connected
            return True
        except:
            self.test_bench_connection = None
            #unable to connect
            return False

    def run_mav(self):
        print "Sono entrato nel run_mav"
        while not self.mav_is_to_disconnect:
            print "Ciclo il run_mav"
            #xa is x data of accelerometer, xg is x data of gyroscope and xm is for magnetometer

            #read imu:
            xa, ya, za, xg, yg, zg, xm, ym, zm = self.mav_connection.read_raw_imu()

            #read attitude
            roll, pitch, yaw, rollspeed, pitchspeed, yawspeed = self.mav_connection.read_attitude()

            #read gps
            #------ to do

            #read pressure
            #------ to do

            #creating database objects
            acc_value = Accelerometer.objects.create(value_x=xa, value_y=ya, value_z=za)
            gyro_value = Gyroscope.objects.create(value_x=xg, value_y=yg, value_z=zg)
            magn_value = Magnetometer.objects.create(value_x=xm, value_y=ym, value_z=zm)
            attitude_value = Attitude.objects.create(roll=roll, pitch=pitch, yaw=yaw)
            #save values
            acc_value.save()
            gyro_value.save()
            magn_value.save()
            attitude_value.save()
            #sleep for half second
            time.sleep(0.5)

        self.mav_connection.close()
        self.mav_connection = None
        self.mav_is_to_disconnect = False

    def run_test_bench(self):
        pass

    def stop_mav(self):
        self.mav_is_to_disconnect = True

    def stop_test_bench(self):
        pass
        self.test_bench_connection.close()

    def is_mav_connected(self):
        #if mav_connection is None then mav is not connected
        if self.mav_connection is None:
            return False
        return True