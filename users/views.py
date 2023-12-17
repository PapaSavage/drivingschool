from django.shortcuts import render, redirect
from django.contrib import messages
from django.db import connection
from django.contrib.auth.decorators import login_required
from .models import Users


# Create your views here.
def home(request):
    return render(request, "users/home.html")


@login_required
def profile(request):
    user_data = Users.objects.get(id_user=request.user.id)
    context = {"user_data": user_data}
    return render(request, "users/profile.html", context=context)
