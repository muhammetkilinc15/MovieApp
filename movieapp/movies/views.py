from django.http import HttpResponse
from django.shortcuts import render
from datetime import date
from movies.models import Movie
from django.shortcuts import get_object_or_404
# Create your views here.
data = {
    "slider": [
        {
            "imageUrl":"slider1.jpg",
            "url":"film-adi-1"
        },
        {
            "imageUrl":"slider2.jpg",
            "url":"film-adi-2"
        },
        {
            "imageUrl":"slider3.jpg",
            "url":"film-adi-3"
        }
    ]
}

def index(request):
    movies = Movie.objects.filter(isActive=True,is_hone=True)
    sliders = data["slider"]
    return  render(request,"index.html",{
        "movies": movies,
        "sliders":sliders
    })

def movies(request):
    movies = Movie.objects.filter(isActive=True)
    return  render(request,"movies.html",{
        "movies":movies
    })

def movie_details(request,slug):
    movie = Movie.objects.filter(slug=slug)[0]
    
    return  render(request,"movies_details.html",{
        "movie":movie,
        "genres":movie.genres.all(),
        "people":movie.people.all()
    })