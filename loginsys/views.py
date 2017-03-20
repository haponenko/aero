# -*- coding: utf-8 -*-
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, redirect
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.template.context_processors import csrf

from loginsys.forms import UserCreateForm


def login(request):
    args = {}
    args.update(csrf(request))
    if request.POST:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/book/')
        else:
            args['login_error'] = "User is not found!"
            return render_to_response('login.html', args)

    else:
        return render_to_response('login.html', args)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


def register(request):
    args = {}
    args.update(csrf(request))
    args['form'] = UserCreateForm()
    if request.POST:
        newuser_form = UserCreateForm(request.POST)
        if newuser_form.is_valid():
            newuser_form.save()
            newuser = auth.authenticate(username=newuser_form.cleaned_data['username'],
                                        password=newuser_form.cleaned_data['password2'])
            auth.login(request, newuser)
            return redirect('/book/')
        else:
            args['form'] = newuser_form
    return render_to_response('register.html', args)
