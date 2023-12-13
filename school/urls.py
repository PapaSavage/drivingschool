from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", views.home, name="home"),
    path("tariffs", views.tariffs, name="tariffs"),
    path("about", views.about, name="about"),
    path(
        "login",
        auth_views.LoginView.as_view(template_name="school/login.html"),
        name="login",
    ),
    path(
        "logout",
        auth_views.LogoutView.as_view(template_name="school/logout.html"),
        name="logout",
    ),
    path("registration", views.registration, name="registration"),
    path("profile", views.profile, name="profile"),
    # path("", views.home, name="home"),
]
