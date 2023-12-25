from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("", views.home, name="instructor_home"),
    path("profile", views.profile, name="instructor_profile"),
    path("schedule", views.schedule, name="instructor_schedule"),
    path("students", views.students, name="instructor_students"),
    path("reports", views.reports, name="instructor_reports"),
    # path("", views.home, name="home"),
]
