from django.conf.urls import patterns, url
from myapp import views

urlpatterns = patterns('',
                       url(r'mav_connection_status/',
                           views.mav_connection_status,
                           name='mav_connection_status'),
                       url(r'close_mav_connection/',
                           views.close_mav_connection,
                           name='close_mav_connection'),
                       url(r'start_mav_connection/',
                           views.start_mav_connection,
                           name='start_mav_connection'),
                       url(r'get_accelerometer/',
                           views.get_accelerometer,
                           name='get_accelerometer'),
                       url(r'get_gyroscope/',
                           views.get_gyroscope,
                           name='get_gyroscope'),
                       url(r'get_magnetometer/',
                           views.get_magnetometer,
                           name='get_magnetometer'),
                       url(r'get_attitude/',
                           views.get_attitude,
                           name='get_attitude'),
                       url(r'^connection',
                           views.ConnectionView.as_view(),
                           name='connection'),
                       url(r'^accelerometer',
                           views.AccelerometerView.as_view(),
                           name='accelerometer'),
                       url(r'^gyroscope',
                           views.GyroscopeView.as_view(),
                           name='gyroscope'),
                       url(r'^magnetometer',
                           views.MagnetometerView.as_view(),
                           name='magnetometer'),
                       url(r'^attitude',
                           views.AttitudeView.as_view(),
                           name='attitude'),
                       url(r'^$',
                           views.HomeView.as_view(),
                           name='home'),
                       )
