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

    def read_raw_imu(self):
        if self.connected:
            msg = self.serial_mav.recv_match(type="RAW_IMU", blocking=True)
            print "Message imu, received:"+str(msg)
            x_acc = msg.xacc/1000.0
            y_acc = msg.yacc/1000.0
            z_acc = msg.zacc/1000.0
            x_gyro = msg.xgyro/1000.0
            y_gyro = msg.ygyro/1000.0
            z_gyro = msg.zgyro/1000.0
            x_mag = msg.xmag/1000.0
            y_mag = msg.ymag/1000.0
            z_mag = msg.zmag/1000.0
            print "Reading IMU successfully"
        else:
            x_acc = 0.01
            y_acc = 0.0
            z_acc = -1.0
            x_gyro = 0.0
            y_gyro = 0.0
            z_gyro = 0.0
            x_mag = 0.0
            y_mag = 0.0
            z_mag = 0.0
        return [x_acc, y_acc, z_acc, x_gyro, y_gyro, z_gyro, x_mag, y_mag, z_mag]

    def read_attitude(self):
        if self.connected:
            msg = self.serial_mav.recv_match(type="ATTITUDE", blocking=True)
            print "Message attitude, received:"+str(msg)
            r = msg.roll
            p = msg.pitch
            y = msg.yaw
            r_s = msg.rollspeed
            p_s = msg.pitchspeed
            y_s = msg.yawspeed
            print "Reading attitude successfully"
        else:
            r = 0
            p = 0
            y = 0
            r_s = 0
            p_s = 0
            y_s = 0
        return [r, p, y, r_s, p_s, y_s]

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