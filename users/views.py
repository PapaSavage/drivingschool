from django.shortcuts import render, redirect
from django.contrib import messages
from django.db import connection
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    return render(request, "users/home.html")


@login_required
def profile(request):
    return render(request, "users/profile.html")
