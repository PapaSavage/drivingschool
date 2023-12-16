from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path("", views.home, name="user_home"),
    path("profile", views.profile, name="profile"),
    # path("", views.home, name="home"),
]
