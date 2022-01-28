from django.shortcuts import render
from .models import client
from .models import Emails

# for regular expressions
import re

# for validating an Email
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'


def home(request):
    posts = client.entries()

    if request.method == 'POST':

        email = request.POST.get('email', None)

        # check if the email is valid
        if (re.fullmatch(regex, email)):

            try:
                #put email in the database
                email_object = Emails.objects.create(email=email)
                email_object.save()

                subscribe_success = "Yay! You have been subscribed. Contact the site owner to unsubscribe."
                return render(request, "home.html", {'posts': posts, 'subscribe_success': subscribe_success})

            except:
                duplicate_email = ":) It seems we already have you on our list. Contact the site owner to unsubscribe."
                return render(request, "home.html", {'posts': posts, 'duplicate_email': duplicate_email})

        else:
            invalid_email = "Enter a valid Email address please :)"
            return render(request, "home.html", {'posts': posts, 'invalid_email': invalid_email})

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

        # check if the email is valid
        if (re.fullmatch(regex, email)):

            try:
                #put email in the database
                email_object = Emails.objects.create(email=email)
                email_object.save()

                subscribe_success = "Yay! You have been subscribed. Contact the site owner to unsubscribe."
                return render(request, "newsletter.html", {'subscribe_success': subscribe_success})

            except:
                duplicate_email = ":) It seems we already have you on our list. Contact the site owner to unsubscribe."
                return render(request, "newsletter.html", {'duplicate_email': duplicate_email})

        else:
            invalid_email = "Enter a valid Email address please :)"
            return render(request, "newsletter.html", {'invalid_email': invalid_email})

    else:
        return render(request, "newsletter.html")


