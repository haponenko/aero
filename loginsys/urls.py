from django.conf.urls import url

import loginsys.views

urlpatterns = [
               # Examples:
               # url(r'^$', 'firstapp.views.home', name='home'),
               # url(r'^blog/', include('blog.urls')),

               url(r'^login/$', loginsys.views.login),
               url(r'^logout/$', loginsys.views.logout),
               url(r'^register/$', loginsys.views.register),
]
