from django.shortcuts import render
from django.http import HttpResponse


def current_datetime(request):
    html = "<html><body><h1>TODO LIST:</h1></body></html>"
    return HttpResponse(html)