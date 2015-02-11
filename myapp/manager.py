from connections import MAVlinkConnection
from models import Accelerometer, Gyroscope, Magnetometer, Attitude
from threading import Lock


class Manager(object):

    __manager_instance = None

    __fast_access_data = None
    __lock = None

    @classmethod
    def get_instance(cls):
        if cls.__manager_instance is None:
            cls.__manager_instance = object.__new__(Manager)
            cls.__manager_instance.__init__()
        return cls.__manager_instance

    def __init__(self):
        #define variable
        self.mav_connection = None
        self.mav_is_to_disconnect = None
        #define lock for external access to fast_access_data
        self.lock = Lock()
        #define dictionary for last data to stream
        self.fast_access_data = {}

    def get_lock(self):
        return self.__lock

    def get_shared_data(self, key):
        #to access here, external class must use get_lock before
        if key in self.__fast_access_data:
            return self.__fast_access_data[key]
        return None

    def start_mav(self):
        #-------------------- define variables --------------------
        self.mav_connection = None
        self.mav_is_to_disconnect = False
        #-------------------- try to connect --------------------
        try:
            self.mav_connection = MAVlinkConnection('/dev/ttyACM0', 115200)
            if self.mav_connection.is_connected():
                return 1
            else:
                self.mav_connection = None
                return 0
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
            #xa is x data of accelerometer, xg is x data of gyroscope and xm is for magnetometer

            #read imu:
            xa, ya, za, xg, yg, zg, xm, ym, zm = self.mav_connection.read_raw_imu()

            #read attitude
            roll, pitch, yaw, rollspeed, pitchspeed, yawspeed = self.mav_connection.read_attitude()

            #read gps
            #------ to do

            #read pressure
            #------ to do

            #update last data in fast_access_data dictionary (first of all get the lock!)
            self.get_lock().acquire()
            self.__fast_access_data['xa'] = xa
            self.__fast_access_data['ya'] = ya
            self.__fast_access_data['za'] = za
            self.__fast_access_data['xg'] = xg
            self.__fast_access_data['yg'] = yg
            self.__fast_access_data['zg'] = zg
            self.__fast_access_data['xm'] = xm
            self.__fast_access_data['ym'] = ym
            self.__fast_access_data['zm'] = zm
            self.__fast_access_data['roll'] = roll
            self.__fast_access_data['pitch'] = pitch
            self.__fast_access_data['yaw'] = yaw
            self.__fast_access_data['rollspeed'] = rollspeed
            self.__fast_access_data['pitchspeed'] = pitchspeed
            self.__fast_access_data['yawspeed'] = yawspeed
            self.get_lock().release()

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

            #time.sleep(0.5)
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