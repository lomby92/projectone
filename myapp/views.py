from django.views import generic
from django.http import HttpResponse

from models import Accelerometer, Gyroscope, Magnetometer, Attitude
from manager import Manager
from datetime import datetime

import thread


class AccelerometerView(generic.base.TemplateView):

    template_name = "myapp/accelerometer.html"


def get_accelerometer(request):
    try:
        Manager.get_instance().get_lock().acquire()
        xa = Manager.get_instance().get_shared_data('xa')
        ya = Manager.get_instance().get_shared_data('ya')
        za = Manager.get_instance().get_shared_data('za')
        t = float(datetime.now().strftime('%Y%m%d%H%M%S%f')[:-3])
        value = [t, xa, ya, za]
        Manager.get_instance().get_lock().release()
    except:
        return HttpResponse("", content_type="text/plain")
    value = str(value)
    return HttpResponse(value, content_type="text/plain")


class GyroscopeView(generic.base.TemplateView):

    template_name = "myapp/gyroscope.html"


def get_gyroscope(request):
    value = Gyroscope.last_value()
    value = str(value)
    return HttpResponse(value, content_type="text/plain")


class MagnetometerView(generic.base.TemplateView):

    template_name = "myapp/magnetometer.html"


def get_magnetometer(request):
    value = Magnetometer.last_value()
    value = str(value)
    return HttpResponse(value, content_type="text/plain")


class AttitudeView(generic.base.TemplateView):

    template_name = "myapp/attitude.html"


def get_attitude(request):
    value = Attitude.last_value()
    value = str(value)
    return HttpResponse(value, content_type="text/plain")


class ConnectionView(generic.base.TemplateView):

    template_name = "myapp/connection.html"


class HomeView(generic.base.TemplateView):

    template_name = "myapp/home.html"


def start_mav_connection(request):
    try:
        #try to connect to drone via mavlink
        val = Manager.get_instance().start_mav()
        if val is 1:
            string = "connected"
            #starting continuous method for get data
            thread.start_new_thread(Manager.get_instance().run_mav, ())
        else:
            string = "unable to connect"
    except:
        string = "error on server"
    return HttpResponse(string, content_type="text/plain")


def close_mav_connection(request):
    try:
        Manager.get_instance().stop_mav()
        return HttpResponse("closed", content_type="text/plain")
    except:
        return HttpResponse("failed to close", content_type="text/plain")


def mav_connection_status(request):
    if Manager.get_instance().is_mav_connected():
        return HttpResponse("OK", content_type="text/plain")
    return HttpResponse("closed", content_type="text/plain")


def start_test_bench_connection(request):
    pass