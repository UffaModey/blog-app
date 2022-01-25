from django.urls import path
from .views import home
from .views import posts
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = "blog"

urlpatterns = [
    path("", home, name="home"),
    path("posts/", posts, name="posts"),
]

urlpatterns += staticfiles_urlpatterns()