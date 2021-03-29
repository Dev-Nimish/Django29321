from django.http import HttpResponse
from django.shortcuts import render
import os

filename = os.path.abspath(__file__)
dirname = os.path.dirname(filename)
parentfile = os.path.dirname(dirname)


def home(request):
    return HttpResponse("<h1>Hello World</h1>")


def page2(request):
    return HttpResponse("<h1>Welcome to the first project.</h1>")


def rend_demo(request):
    return render(request, "sample.html")


def sam_demo(request):
    return render(request, "html_demo/sample.html")
