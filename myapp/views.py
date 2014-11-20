import djqscsv
import thread

from django.views import generic
from django.http import HttpResponse

from models import Accelerometer
from manager import Manager


class AccelerometerView(generic.base.TemplateView):

    template_name = "myapp/accelerometer.html"


def get_accelerometer(request):
    value = Accelerometer.last_value()
    return HttpResponse(str(value), content_type="text/plain")


class ConnectionView(generic.base.TemplateView):

    template_name = "myapp/connection.html"


class HomeView(generic.base.TemplateView):

    template_name = "myapp/home.html"


def start_connection(request):
    try:
        thread.start_new_thread(Manager, ())
        string = "OK"
    except:
        string = "NOT CONNECTED"
    return HttpResponse(string, content_type="text/plain")