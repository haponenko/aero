from django.conf.urls import patterns, include, url

import article.views

urlpatterns = [

    url(r'^all/$', article.views.articles),
    url(r'^get/(?P<article_id>\d+)/$', article.views.article),
    url(r'^addlike/(?P<article_id>\d+)/$', article.views.addlike),
    url(r'^addcomment/(?P<article_id>\d+)/$', article.views.addcomment),
    url(r'^page/(\d+)/$', article.views.articles),
    url(r'^', article.views.articles),
]
