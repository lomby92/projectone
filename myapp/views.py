from django.shortcuts import render
from django.views import generic


class AccelerometerView(generic.base.TemplateView):

    template_name = "myapp/accelerometer.html"


class ConnectionView(generic.base.TemplateView):

    template_name = "myapp/connection.html"

class HomeView(generic.base.TemplateView):

    template_name = "myapp/home.html"