from django.shortcuts import render, redirect
from django.contrib import messages
from django.db import connection
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from usertype import *


# Create your views here.
def home(request):
    if admin_exist(request):
        return redirect("admin_home")

    elif instructor_exist(request):
        return redirect("instructor_home")

    elif lecture_exist(request):
        return redirect("lector_home")

    elif student_exist(request):
        return redirect("student_home")

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


@login_required
def user_tariffs(request):
    with connection.cursor() as cursor:
        cursor.execute(
            "Select PlansEducations.name, PlansEducations.Theoretical_time, PlansEducations.Practise_time, DrivingCategories.price, DrivingCategories.name, PlansEducations.ID_plan from PlansEducations join DrivingCategories on DrivingCategories.ID_category = PlansEducations.ID_category"
        )
        rows = cursor.fetchall()
        plans_educations = []
        for row in rows:
            plans_educations.append(row)
        data = {
            "plans_educations": plans_educations,
        }
    if request.method == "POST":
        idplan = request.POST.get("idplan")
        try:
            with connection.cursor() as cursor:
                query = f"Insert IGNORE into Students (ID_student) values ({request.user.id})"
                cursor.execute(query)
                query = "Insert into Contracts (DateContractStart, ID_student, ID_plan) values (NOW(), %s, %s)"
                vals = (request.user.id, idplan)
                cursor.execute(query, vals)
                connection.commit()

                messages.success(request, f"План обучения выбран!")
        except:
            messages.error(request, f"Ошибка при работе с базой данных.")

    return render(request, "users/tariffs.html", context=data)


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
