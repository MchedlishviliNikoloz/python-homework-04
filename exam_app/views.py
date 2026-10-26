from django.shortcuts import render

# Create your views here.

def home(request):
    context = {}

    return render(request, "home.html", context)

def films(request):
    movies = [
        {"title": "A Bronx Tale", "imdb": 9.1},
        {"title": "Inception", "imdb": 9.0},
        {"title": "The Wolf of Wall Street", "imdb": 9.2},
        {"title": "The Green Mile", "imdb": 8.7},
        {"title": "Grown Ups", "imdb": 8.9},
        {"title": "The Founder", "imdb": 8.5},
        {"title": "Interstellar", "imdb": 9.0},
        {"title": "The Prestige", "imdb": 8.7},
        {"title": "The Hangover", "imdb": 9.0},
        {"title": "Red Notice", "imdb": 7.8},
    ]

    context = {
        "movies": movies,
    }

    return render(request, "films.html", context)