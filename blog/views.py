from django.shortcuts import render
from .models import client

def home(request):

    posts = client.entries()
    return render(request, "home.html", {'posts': posts})

def posts(request):
    posts = client.entries()
    return render(request, "posts.html", {'posts': posts})

def article(request, slug):
    posts = client.entries()

    for article in posts:
        if (article.slug == slug):
            return render(request, "article.html", {'article': article})


