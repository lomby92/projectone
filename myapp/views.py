import djqscsv

from django.views import generic

from models import Accelerometer
from utils import create_accelerometer_value


class AccelerometerView(generic.base.TemplateView):

    template_name = "myapp/accelerometer.html"


class ConnectionView(generic.base.TemplateView):

    template_name = "myapp/connection.html"


class HomeView(generic.base.TemplateView):

    template_name = "myapp/home.html"


def get_accelerometer_csv(request):
    # now create a random accelerometer values
    create_accelerometer_value()
    # elaborate request
    last_set = None
    try:
        qs = Accelerometer.objects.order_by('id')
        last_set = qs.all().reverse()[:1]
    except:
        pass
    return djqscsv.render_to_csv_response(last_set)