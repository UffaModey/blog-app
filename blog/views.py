from django.shortcuts import render
from .models import client

def home(request):

    posts = client.entries()
    return render(request, "home.html", {'posts': posts})