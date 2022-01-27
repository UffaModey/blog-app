from django.shortcuts import render
from .models import client

def home(request):

    posts = client.entries()
    return render(request, "home.html", {'posts': posts})

def posts(request):
    posts = client.entries()
    return render(request, "posts.html", {'posts': posts})

def article(request, slug, image_id):
    posts = client.entries()
    assets = client.asset(image_id)

    for article in posts:
        if (article.slug == slug):
            image_url = assets.url()

            return render(request, "article.html", {'article': article, 'image_url': image_url}, )


