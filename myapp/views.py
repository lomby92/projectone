from django.views import generic
from django.http import HttpResponse

from models import Accelerometer
from manager import Manager

import thread


class AccelerometerView(generic.base.TemplateView):

    template_name = "myapp/accelerometer.html"


def get_accelerometer(request):
    value = Accelerometer.last_value()
    value = str(value)
    return HttpResponse(value, content_type="text/plain")


class ConnectionView(generic.base.TemplateView):

    template_name = "myapp/connection.html"


class HomeView(generic.base.TemplateView):

    template_name = "myapp/home.html"


def start_mav_connection(request):
    try:
        val = Manager.get_instance().start_mav()
        if val is 1:
            string = "connected"
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
        pass
        return HttpResponse("failed to close", content_type="text/plain")




def start_test_bench_connection(request):
    pass