from django.urls import path
from .views import home
from .views import posts
from .views import article
from .views import newsletter
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


app_name = "blog"

urlpatterns = [
    path("", home, name="home"),
    path("posts/", posts, name="posts"),
    path("posts/<slug:slug>/<str:image_id>/", article, name="article"),
    path("newsletter/", newsletter, name="newsletter"),
]

urlpatterns += staticfiles_urlpatterns()