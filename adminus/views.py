from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.db import connection
from django.contrib.auth.decorators import login_required
import sys

sys.path.append(r"D:\Projects\drivingschool")
from users.models import Users
from usertype import *

links_admin_home = [
    {
        "url": "admin_home",
        "name_block": "active",
        "title": "Главная",
        "icon_class": "fas fa-house-user fa-fw me-1",
    },
    {
        "url": "admin_profile",
        "name_block": "link-body-emphasis",
        "title": "Личный кабинет",
        "icon_class": "fas fa-child fa-fw me-1",
    },
    {
        "url": "admin_instructors",
        "name_block": "link-body-emphasis",
        "title": "Инструкторы",
        "icon_class": "fas fa-biking fa-fw me-1",
    },
]
links_admin_profile = [
    {
        "url": "admin_home",
        "name_block": "link-body-emphasis",
        "title": "Главная",
        "icon_class": "fas fa-house-user fa-fw me-1",
    },
    {
        "url": "admin_profile",
        "name_block": "active",
        "title": "Личный кабинет",
        "icon_class": "fas fa-child fa-fw me-1",
    },
    {
        "url": "admin_instructors",
        "name_block": "link-body-emphasis",
        "title": "Инструкторы",
        "icon_class": "fas fa-biking fa-fw me-1",
    },
]

links_admin_instructors = [
    {
        "url": "admin_home",
        "name_block": "link-body-emphasis",
        "title": "Главная",
        "icon_class": "fas fa-house-user fa-fw me-1",
    },
    {
        "url": "admin_profile",
        "name_block": "link-body-emphasis",
        "title": "Личный кабинет",
        "icon_class": "fas fa-child fa-fw me-1",
    },
    {
        "url": "admin_instructors",
        "name_block": "active",
        "title": "Инструкторы",
        "icon_class": "fas fa-biking fa-fw me-1",
    },
]


# Create your views here.
@login_required
def home(request):
    if admin_exist(request):
        data = {"links": links_admin_home}

        return render(request, "adminus/home.html", context=data)
    else:
        messages.error(request, f"У вас нет доступа к этой ссылке")
        return redirect("user_home")


@login_required
def instructors(request):
    if admin_exist(request):
        data = {"links": links_admin_instructors}

        return render(request, "adminus/instructors.html", context=data)
    else:
        messages.error(request, f"У вас нет доступа к этой ссылке")
        return redirect("user_home")


@login_required
def profile(request):
    user_data = Users.objects.get(id_user=request.user.id)
    if admin_exist(request):
        links = {"links": links_admin_profile}
    else:
        messages.error(request, f"У вас нет доступа к этой ссылке")
        return redirect("user_home")

    user_data = {"user_data": user_data} | links

    if request.method == "POST":
        surname = request.POST.get("surname")
        firstname = request.POST.get("firstname")
        secondname = request.POST.get("secondname")
        adress = request.POST.get("adress")
        phone = request.POST.get("phone")
        date = request.POST.get("date")
        passport = request.POST.get("passport")
        medicalcertificate = request.POST.get("medicalcertificate")
        email = request.POST.get("email")

        try:
            with connection.cursor() as cursor:
                query = "Update Users Set Surname = %s, Name = %s, SecondName = %s, Adress = %s, Telephone = %s, DateOfBirth = %s, Passport = %s, SeriaMedicalCertificate = %s, email = %s where id_user = %s"
                vals = (
                    surname,
                    firstname,
                    secondname,
                    adress,
                    phone,
                    date,
                    passport,
                    medicalcertificate,
                    email,
                    request.user.id,
                )
                cursor.execute(query, vals)
                connection.commit()
            messages.success(request, f"Изменения успешно сохранены.")
        except:
            messages.error(request, f"Ошибка сохранения данных.")

    return render(request, "users/profile.html", context=user_data)
