from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, Http404

# Create your views here.

def index(request):
    return HttpResponse("Web Page women")


def categories(request, cat_id):
    return HttpResponse(f"<h1>Web Page Categories</h1><p>id: {cat_id}</p>")

def categories_by_slug(request, cat_slug):
    return HttpResponse(f"<h1>Web Page Categories</h1><p>slug: {cat_slug}</p>")

def archive(request, year):
    if  year > 2024:
        raise Http404()
    return HttpResponse(f"<h1>Year archive:</h1><p>year: {year}</p>")

def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Page not Found</h1>")