from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("", views.home, name="admin_home"),
    path("profile", views.profile, name="admin_profile"),
    path("instructors", views.instructors, name="admin_instructors"),
    # path("", views.home, name="home"),
]
