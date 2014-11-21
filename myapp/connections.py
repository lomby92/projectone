from pymavlink import mavutil
import serial


class MAVlinkConnection():

    def __init__(self, port, baud_rate):
        try:
            self.serial_mav = mavutil.mavlink_connection(port, baud_rate)
            self.port = port
            self.rate = baud_rate
            self.connected = True
            self.work_frequency = 10
            self.serial_mav.wait_heartbeat()
        except Exception:
            self.serial_mav = None
            self.work_frequency = 10
            self.port = None
            self.rate = None
            self.connected = False

    def send_message(self, message):
        #not implemented yet
        pass

    def get_freq(self):
        return self.work_frequency

    def is_connected(self):
        return self.connected

    def read_accelerometer(self):
        if self.connected:
            assert isinstance(self.serial_mav, object)
            msg = self.serial_mav.recv_match(type="RAW_IMU", blocking=True)
            x_acc = msg.xacc/1000.0
            y_acc = msg.yacc/1000.0
            z_acc = msg.zacc/1000.0
        else:
            x_acc = 0.0
            y_acc = 0.0
            z_acc = -1.0
        return [x_acc, y_acc, z_acc]

    def close(self):
        if self.connected:
            assert isinstance(self.serial_mav, object)
            self.serial_mav.close()


class TestBenchConnection():

    def __init__(self, port, baud_rate):
        try:
            self.port = port
            self.baud_rate = baud_rate
            self.serial_test_bench = serial.Serial(port=self.port, baudrate=self.baud_rate)
            self.connected = True
            self.work_frequency = 10
            #value to update
            self.msg_length = 15
        except:
            self.serial_test_bench = None
            self.work_frequency = 10
            #value to update
            self.msg_length = 15
            self.port = None
            self.rate = None
            self.connected = False

    def read_all_by_serial(self):
        if self.connected:
            assert isinstance(self.serial_test_bench, serial.Serial)
            msg = self.serial_test_bench.read(self.msg_length)
            #do something with msg
            return msg
        else:
            return None

    def get_freq(self):
        return self.work_frequency

    def is_connected(self):
        return self.connected

    def close(self):
        if self.connected:
            assert isinstance(self.serial_test_bench, serial.Serial)
            self.serial_test_bench.close()