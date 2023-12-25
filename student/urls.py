from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("", views.home, name="student_home"),
    path("profile", views.profile, name="student_profile"),
    path("study", views.study, name="student_study"),
    path("schedule", views.schedule, name="student_schedule"),
    path("tests", views.tests, name="student_tests"),
    path("exams", views.exams, name="student_exams"),
    path("messages", views.message, name="student_messages"),
    # path("", views.home, name="home"),
]
