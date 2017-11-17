# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from login_app.forms import UserBasicForm, AdditionalForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, 'login_app/index.html')

def user_register(request):
    registered = False

    if request.method == "POST":
        basic_form = UserBasicForm(data=request.POST)
        additional_form = AdditionalForm(data=request.POST)

        if basic_form.is_valid() and additional_form.is_valid():
            basic = basic_form.save()
            basic.set_password(basic.password)
            basic.save()

            addition = additional_form.save(commit=False)
            addition.user = basic

            if 'profile_pic' in request.FILES:
                print('There is a picture')
                addition.profile_pic = request.FILES['profile_pic']

            addition.save()
            registered = True
        else:
            print (basic_form.errors, additional_form.errors)

    else:
        basic_form = UserBasicForm
        additional_form = AdditionalForm

    return render(request, 'login_app/register.html', {'basic_form': basic_form, 'additional_form': additional_form, 'register': registered})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("User is not active")
        else:
            return HttpResponse('Invalid information')
    else:
        return render(request, 'login_app/login.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
