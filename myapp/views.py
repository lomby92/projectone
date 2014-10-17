import djqscsv

from django.views import generic

from models import Accelerometer
from utils import save_csv


class AccelerometerView(generic.base.TemplateView):

    template_name = "myapp/accelerometer.html"


class ConnectionView(generic.base.TemplateView):

    template_name = "myapp/connection.html"


class HomeView(generic.base.TemplateView):

    template_name = "myapp/home.html"


def get_csv(request):
    save_csv()
    last_set = None
    try:
        last_set = Accelerometer.objects.order_by('-id').first()
    except:
        pass
    return djqscsv.render_to_csv_response(last_set)