from django.shortcuts import render
from fly.models import *

# Create your views here.

from django.http import HttpResponse


def homePageView(request):
    return HttpResponse("Hello, Fly!")



