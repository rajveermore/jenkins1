from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(r):
    return HttpResponse("<h1> this is jenkin test</h1>")