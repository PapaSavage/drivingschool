from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.db import connection
from django.contrib.auth.decorators import login_required
import sys

sys.path.append(r"D:\Projects\drivingschool")
from users.models import Users
from usertype import *

links_lecture_home = [
    {
        "url": "lecture_home",
        "name_block": "active",
        "title": "Главная",
        "icon_class": "fas fa-house-user fa-fw me-1",
    },
    {
        "url": "lecture_profile",
        "name_block": "link-body-emphasis",
        "title": "Личный кабинет",
        "icon_class": "fas fa-child fa-fw me-1",
    },
    {
        "url": "lecture_schedule",
        "name_block": "link-body-emphasis",
        "title": "Расписание занятий",
        "icon_class": "fas fa-clipboard-list fa-fw me-1",
    },
    {
        "url": "lecture_students",
        "name_block": "link-body-emphasis",
        "title": "Ученики",
        "icon_class": "fas fa-user-graduate fa-fw me-1",
    },
    {
        "url": "lecture_reports",
        "name_block": "link-body-emphasis",
        "title": "Отчетность",
        "icon_class": "fas fa-flag fa-fw me-1",
    },
]
links_lecture_home = [
    {
        "url": "lecture_home",
        "name_block": "active",
        "title": "Главная",
        "icon_class": "fas fa-house-user fa-fw me-1",
    },
    {
        "url": "lecture_profile",
        "name_block": "link-body-emphasis",
        "title": "Личный кабинет",
        "icon_class": "fas fa-child fa-fw me-1",
    },
    {
        "url": "lecture_schedule",
        "name_block": "link-body-emphasis",
        "title": "Расписание занятий",
        "icon_class": "fas fa-clipboard-list fa-fw me-1",
    },
    {
        "url": "lecture_students",
        "name_block": "link-body-emphasis",
        "title": "Ученики",
        "icon_class": "fas fa-user-graduate fa-fw me-1",
    },
    {
        "url": "lecture_reports",
        "name_block": "link-body-emphasis",
        "title": "Отчетность",
        "icon_class": "fas fa-flag fa-fw me-1",
    },
]
links_lecture_profile = [
    {
        "url": "lecture_home",
        "name_block": "link-body-emphasis",
        "title": "Главная",
        "icon_class": "fas fa-house-user fa-fw me-1",
    },
    {
        "url": "lecture_profile",
        "name_block": "active",
        "title": "Личный кабинет",
        "icon_class": "fas fa-child fa-fw me-1",
    },
    {
        "url": "lecture_schedule",
        "name_block": "link-body-emphasis",
        "title": "Расписание занятий",
        "icon_class": "fas fa-clipboard-list fa-fw me-1",
    },
    {
        "url": "lecture_students",
        "name_block": "link-body-emphasis",
        "title": "Ученики",
        "icon_class": "fas fa-user-graduate fa-fw me-1",
    },
    {
        "url": "lecture_reports",
        "name_block": "link-body-emphasis",
        "title": "Отчетность",
        "icon_class": "fas fa-flag fa-fw me-1",
    },
]
links_lecture_schedule = [
    {
        "url": "lecture_home",
        "name_block": "link-body-emphasis",
        "title": "Главная",
        "icon_class": "fas fa-house-user fa-fw me-1",
    },
    {
        "url": "lecture_profile",
        "name_block": "link-body-emphasis",
        "title": "Личный кабинет",
        "icon_class": "fas fa-child fa-fw me-1",
    },
    {
        "url": "lecture_schedule",
        "name_block": "active",
        "title": "Расписание занятий",
        "icon_class": "fas fa-clipboard-list fa-fw me-1",
    },
    {
        "url": "lecture_students",
        "name_block": "link-body-emphasis",
        "title": "Ученики",
        "icon_class": "fas fa-user-graduate fa-fw me-1",
    },
    {
        "url": "lecture_reports",
        "name_block": "link-body-emphasis",
        "title": "Отчетность",
        "icon_class": "fas fa-flag fa-fw me-1",
    },
]
links_lecture_students = [
    {
        "url": "lecture_home",
        "name_block": "link-body-emphasis",
        "title": "Главная",
        "icon_class": "fas fa-house-user fa-fw me-1",
    },
    {
        "url": "lecture_profile",
        "name_block": "link-body-emphasis",
        "title": "Личный кабинет",
        "icon_class": "fas fa-child fa-fw me-1",
    },
    {
        "url": "lecture_schedule",
        "name_block": "link-body-emphasis",
        "title": "Расписание занятий",
        "icon_class": "fas fa-clipboard-list fa-fw me-1",
    },
    {
        "url": "lecture_students",
        "name_block": "active",
        "title": "Ученики",
        "icon_class": "fas fa-user-graduate fa-fw me-1",
    },
    {
        "url": "lecture_reports",
        "name_block": "link-body-emphasis",
        "title": "Отчетность",
        "icon_class": "fas fa-flag fa-fw me-1",
    },
]
links_lecture_reports = [
    {
        "url": "lecture_home",
        "name_block": "link-body-emphasis",
        "title": "Главная",
        "icon_class": "fas fa-house-user fa-fw me-1",
    },
    {
        "url": "lecture_profile",
        "name_block": "link-body-emphasis",
        "title": "Личный кабинет",
        "icon_class": "fas fa-child fa-fw me-1",
    },
    {
        "url": "lecture_schedule",
        "name_block": "link-body-emphasis",
        "title": "Расписание занятий",
        "icon_class": "fas fa-clipboard-list fa-fw me-1",
    },
    {
        "url": "lecture_students",
        "name_block": "link-body-emphasis",
        "title": "Ученики",
        "icon_class": "fas fa-user-graduate fa-fw me-1",
    },
    {
        "url": "lecture_reports",
        "name_block": "active",
        "title": "Отчетность",
        "icon_class": "fas fa-flag fa-fw me-1",
    },
]


# Create your views here.
@login_required
def home(request):
    if lecture_exist(request):
        data = {"links": links_lecture_home}

        return render(request, "lecture/home.html", context=data)
    else:
        messages.error(request, f"У вас нет доступа к этой ссылке")
        return redirect("user_home")


@login_required
def schedule(request):
    if lecture_exist(request):
        data = {"links": links_lecture_schedule}

        return render(request, "lecture/dev.html", context=data)
    else:
        messages.error(request, f"У вас нет доступа к этой ссылке")
        return redirect("user_home")


@login_required
def students(request):
    if lecture_exist(request):
        data = {"links": links_lecture_students}

        return render(request, "lecture/dev.html", context=data)
    else:
        messages.error(request, f"У вас нет доступа к этой ссылке")
        return redirect("user_home")


@login_required
def reports(request):
    if lecture_exist(request):
        data = {"links": links_lecture_reports}

        return render(request, "lecture/dev.html", context=data)
    else:
        messages.error(request, f"У вас нет доступа к этой ссылке")
        return redirect("user_home")


def profile(request):
    user_data = Users.objects.get(id_user=request.user.id)
    if lecture_exist(request):
        links = {"links": links_lecture_profile}
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
