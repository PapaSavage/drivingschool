from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("", views.home, name="lecture_home"),
    path("profile", views.profile, name="lecture_profile"),
    path("schedule", views.schedule, name="lecture_schedule"),
    path("students", views.students, name="lecture_students"),
    path("reports", views.reports, name="lecture_reports"),
    # path("", views.home, name="home"),
]
