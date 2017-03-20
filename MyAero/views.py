from django.shortcuts import render_to_response
from django.contrib import auth


def home_page(request):
    return render_to_response('home.html', {'username': auth.get_user(request).username})


def about_page(request):
    return render_to_response('about.html', {'username': auth.get_user(request).username})
