from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect
from django.urls import reverse


# Create your views here.

def index(request):
    return HttpResponse("Web Page women")


def categories(request, cat_id):
    return HttpResponse(f"<h1>Web Page Categories</h1><p>id: {cat_id}</p>")

def categories_by_slug(request, cat_slug):
    return HttpResponse(f"<h1>Web Page Categories</h1><p>slug: {cat_slug}</p>")

def archive(request, year):
    if year > 2024:
        uri = reverse('cats', args=('music', ))
        return redirect(uri)
    return HttpResponse(f"<h1>Year archive:</h1><p>year: {year}</p>")

def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Page not Found</h1>")