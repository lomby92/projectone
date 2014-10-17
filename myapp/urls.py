from django.conf.urls import patterns, url
from myapp import views

urlpatterns = patterns('',
                       url(r'get_csv/',
                           views.get_csv,
                           name='get_csv'),
                       url(r'^connection',
                           views.ConnectionView.as_view(),
                           name='connection'),
                       url(r'^accelerometer',
                           views.AccelerometerView.as_view(),
                           name='accelerometer'),
                       url(r'^$',
                           views.HomeView.as_view(),
                           name='home'),
                       )