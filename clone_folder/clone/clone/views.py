from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.conf import settings
from . import models
from . import logic
from datetime import date


def login_page(request):
    '''Navigates to login page.'''
    return render(request, 'clone/login.html')