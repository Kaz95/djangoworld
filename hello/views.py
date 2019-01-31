from django.http import HttpResponse
from django.shortcuts import render


def my_view(request):
    return HttpResponse('Hello, World!')


def home_view(request):
    return HttpResponse('Home')
