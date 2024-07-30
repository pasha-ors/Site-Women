from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Web Page women")


def categories(request, cat_id):
    return HttpResponse(f"<h1>Web Page Categories</h1><p>id: {cat_id}</p>")

def categories_by_slug(request, cat_slug):
    return HttpResponse(f"<h1>Web Page Categories</h1><p>slug: {cat_slug}</p>")

def archive(request, year):
    return HttpResponse(f"<h1>Year archive:</h1><p>year: {year}</p>")