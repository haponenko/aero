from django.conf.urls import url, include
from django.contrib import admin

import MyAero.views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^auth/', include('loginsys.urls')),
    url(r'^about/', MyAero.views.about_page),
    url(r'^articles/', include('article.urls')),
    url(r'^book/', include('booking.urls')),
    url(r'^', MyAero.views.home_page),
]
