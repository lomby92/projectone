from pymavlink import mavutil


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