from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.


def index(request):
    return  HttpResponse("Index")

def movies(request):
    return  HttpResponse("Movies")

def movie_details(request,slug):
    return  HttpResponse("Movie_details "+slug)