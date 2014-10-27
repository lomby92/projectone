import djqscsv
import thread

from django.views import generic
from django.http import HttpResponse

from models import Accelerometer
from manager import Manager


class AccelerometerView(generic.base.TemplateView):

    template_name = "myapp/accelerometer.html"


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


def get_accelerometer_csv(request):
    last_set = None
    try:
        qs = Accelerometer.objects.order_by('id')
        last_set = qs.all().reverse()[:1]
    except:
        pass
    return djqscsv.render_to_csv_response(last_set)