from django.shortcuts import render
from .models import client
from .models import Emails

def home(request):
    posts = client.entries()

    if request.method == 'POST':

        email = request.POST.get('email', None)

        #put email in the database
        email_object = Emails.objects.create(email=email)
        email_object.save()

        return render(request, "home.html", {'posts': posts})

    else:
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

            return render(request, "article.html", {'article': article, 'image_url': image_url} )

def newsletter(request):
    if request.method == 'POST':
        email = request.POST.get('emailn', None)

        #put email in the database
        email_object = Emails.objects.create(email=email)
        email_object.save()
        return render(request, "newsletter.html")

    else:
        return render(request, "newsletter.html")


