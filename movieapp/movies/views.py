from django.http import HttpResponse
from django.shortcuts import render
from datetime import date

# Create your views here.
data = {
    "movies": [
        {
        "title":"Film adı 1",
         "coverImage":"cover3.jpg",
        "description":"film aciklama 1",
        "imageUrl":"m1.jpg",
        "slug":"film-adi-1",
        "language":"english",
        "date":date(2021,10,10)
        },
        {
        "title":"Film adı 2",
         "coverImage":"cover2.jpg",
        "description":"film aciklama 2",
        "imageUrl":"m2.jpg",
        "slug":"film-adi-2",
        "language":"english",
        "date":date(2024,3,9)
        },
        {
        "title":"Film adı 3",
         "coverImage":"cover1.jpg",
        "description":"film aciklama 3",
        "imageUrl":"m3.jpg",
        "slug":"film-adi-3",
        "language":"english",
        "date":date(2019,5,25)
        },
        {
        "title":"Film adı 4",
         "coverImage":"cover1.jpg",
        "description":"film aciklama 4",
        "imageUrl":"m4.jpg",
        "slug":"film-adi-4",
        "language":"english",
        "date":date(2014,5,25)
        },
        {
        "title":"Film adı 5",
         "coverImage":"cover2.jpg",
        "description":"film aciklama 4",
        "imageUrl":"m2.jpg",
        "slug":"film-adi-4",
        "language":"english",
        "date":date(2014,5,25)
        },
        {
        "title":"Film adı 6",
         "coverImage":"cover3.jpg",
        "description":"film aciklama 4",
        "imageUrl":"m1.jpg",
        "slug":"film-adi-4",
        "language":"english",
        "date":date(2014,5,25)
        },
    
    ],
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
    movies = data["movies"][-4:]
    sliders = data["slider"]
    return  render(request,"index.html",{
        "movies": movies,
        "sliders":sliders
    })

def movies(request):
    movies = data["movies"]
    return  render(request,"movies.html",{
        "movies":movies
    })

def movie_details(request,slug):
    movies = data["movies"]
    selectedMovie = next(movie for movie in movies if movie["slug"]==slug) #  bir liste anlama (list comprehension) ifadesi kullanarak, movies listesindeki belirli bir koşulu sağlayan ilk filmi(next) ile  bulur.
    return  render(request,"movies_details.html",{
        "movie":selectedMovie
    })