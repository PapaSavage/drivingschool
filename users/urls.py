from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("", views.home, name="user_home"),
    path("profile", views.profile, name="profile"),
    path("tariffs", views.user_tariffs, name="user_tariffs"),
    # path("", views.home, name="home"),
]
