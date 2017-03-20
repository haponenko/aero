from django.conf.urls import url
from django.contrib import admin

import booking.views

urlpatterns = [
    url(r'^state_out_ajax/$', booking.views.state_out_ajax, name='state_out_ajax'),
    url(r'^city_out_ajax/$', booking.views.city_out_ajax, name='city_out_ajax'),
    url(r'^state_in_ajax/$', booking.views.state_in_ajax, name='state_in_ajax'),
    url(r'^city_in_ajax/$', booking.views.city_in_ajax, name='city_in_ajax'),
    url(r'^success/$', booking.views.success),
    url(r'^', booking.views.add_booker),
]
