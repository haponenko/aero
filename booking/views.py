# coding=utf-8
import json

from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from django.shortcuts import render, render_to_response
from django.contrib import auth
from booking.forms import BookForm
from booking.models import State, City, Country



def success(request):
    return render_to_response('success.html', {'username': auth.get_user(request).username})


def add_booker(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        #if form.is_valid():
        #email = form.cleaned_data['email']
        email = request.POST['email']

        countryout = Country.objects.get(pk=request.POST['country_out'])
        countryin = Country.objects.get(pk=request.POST['country_in'])
        stateout = State.objects.get(pk=request.POST['state_out'])
        statein = State.objects.get(pk=request.POST['state_in'])
        cityout = City.objects.get(pk=request.POST['city_out'])
        cityin = City.objects.get(pk=request.POST['city_in'])

        subject = u"Your Ticket Order. We will contact with you!"
        message = u"Name: %s" % request.POST['firstname']
        message += u"\nSurname: %s" % request.POST['surname']
        message += u"\nDate out: %s" % request.POST['date_in']
        message += u"\nDate in: %s" % request.POST['date_out']
        message += u"\nCountry out: %s" % countryout
        message += u"\nState out: %s" % stateout
        message += u"\nCity out: %s" % cityout
        message += u"\nCountry in: %s" % countryin
        message += u"\nState in: %s" % statein
        message += u"\nCity in: %s" % cityin

        from_email = settings.EMAIL_HOST_USER
        to_list = [email, settings.EMAIL_HOST_USER]
        send_mail(subject, message, from_email, to_list, fail_silently=True)
        #form.save()
        return HttpResponseRedirect('../success/')
    else:
        form = BookForm()

    return render(request, 'booking.html', {'form': form, 'username': auth.get_user(request).username,})


def state_out_ajax(request):
    if request.POST and request.is_ajax():
        c_id = request.POST.get('country_id')
        state = State.objects.filter(country_id=c_id)
        state_dict = {}
        for state in state:
            state_dict[state.id] = state.name
        print state_dict, json.dumps(state_dict)
        return JsonResponse(state_dict, content_type="application/json")  # shortcut for json.dumps


def city_out_ajax(request):
    if request.POST and request.is_ajax():
        s_id = request.POST.get('state_id')
        city = City.objects.filter(state_id=s_id)
        city_dict = {}
        for city in city:
            city_dict[city.id] = city.name
        return HttpResponse(json.dumps(city_dict), content_type="application/json")


def state_in_ajax(request):
    if request.POST and request.is_ajax():
        c_id = request.POST.get('country_id')
        state = State.objects.filter(country_id=c_id)
        state_dict = {}
        for state in state:
            state_dict[state.id] = state.name
        print state_dict, json.dumps(state_dict)
        return JsonResponse(state_dict, content_type="application/json")  # shortcut for json.dumps


def city_in_ajax(request):
    if request.POST and request.is_ajax():
        s_id = request.POST.get('state_id')
        city = City.objects.filter(state_id=s_id)
        city_dict = {}
        for city in city:
            city_dict[city.id] = city.name
        return HttpResponse(json.dumps(city_dict), content_type="application/json")
