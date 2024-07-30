from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Web Page women")


def categories(request):
    return HttpResponse("<h1>Web Page Categories</h1>")