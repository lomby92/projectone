from django.conf.urls import patterns, url
from myapp import views

urlpatterns = patterns('',
                       url(r'start_mav_connection/',
                           views.start_mav_connection,
                           name='start_mav_connection'),
                       url(r'get_accelerometer/',
                           views.get_accelerometer,
                           name='get_accelerometer'),
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
