from django.shortcuts import render, redirect
from django.contrib import messages
from django.db import connection
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    return render(request, "school/home.html")


def tariffs(request):
    with connection.cursor() as cursor:
        cursor.execute(
            "Select PlansEducations.name, PlansEducations.Theoretical_time, PlansEducations.Practise_time, DrivingCategories.price, DrivingCategories.name from PlansEducations join DrivingCategories on DrivingCategories.ID_category = PlansEducations.ID_category"
        )
        rows = cursor.fetchall()
        plans_educations = []
        for row in rows:
            plans_educations.append(row)
        print(rows)
        data = {
            "plans_educations": plans_educations,
        }

    return render(request, "school/tariffs.html", context=data)


def about(request):
    return render(request, "school/about.html")


def login(request):
    return render(request, "school/login.html")


def logout(request):
    return render(request, "school/logout.html")


def registration(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"Ваш аккаунт создан: можно войти на сайт.")
            return redirect("login")
    else:
        form = UserRegisterForm()
    return render(request, "school/registration.html", {"form": form})


@login_required
def profile(request):
    return render(request, "school/profile.html")
