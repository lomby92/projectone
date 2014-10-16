import json

from django.http import HttpResponse
from django.views import generic

from myapp.models import Accelerometer


class AccelerometerView(generic.base.TemplateView):

    template_name = "myapp/accelerometer.html"


class ConnectionView(generic.base.TemplateView):

    template_name = "myapp/connection.html"


class HomeView(generic.base.TemplateView):

    template_name = "myapp/home.html"


def accelerometer_json(request):
    data = {"x":"zero"}
    return HttpResponse(data, content_type='application/json')