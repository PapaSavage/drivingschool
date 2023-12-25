from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.db import connection
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import sys

sys.path.append(r"D:\Projects\drivingschool")
from users.models import Users
from usertype import *

links_instructor_home = [
    {
        "url": "instructor_home",
        "name_block": "active",
        "title": "Главная",
        "icon_class": "fas fa-house-user fa-fw me-1",
    },
    {
        "url": "instructor_profile",
        "name_block": "link-body-emphasis",
        "title": "Личный кабинет",
        "icon_class": "fas fa-child fa-fw me-1",
    },
    {
        "url": "instructor_schedule",
        "name_block": "link-body-emphasis",
        "title": "Расписание занятий",
        "icon_class": "fas fa-clipboard-list fa-fw me-1",
    },
    {
        "url": "instructor_students",
        "name_block": "link-body-emphasis",
        "title": "Ученики",
        "icon_class": "fas fa-user-graduate fa-fw me-1",
    },
    {
        "url": "instructor_reports",
        "name_block": "link-body-emphasis",
        "title": "Отчетность",
        "icon_class": "fas fa-flag fa-fw me-1",
    },
]
links_instructor_profile = [
    {
        "url": "instructor_home",
        "name_block": "link-body-emphasis",
        "title": "Главная",
        "icon_class": "fas fa-house-user fa-fw me-1",
    },
    {
        "url": "instructor_profile",
        "name_block": "active",
        "title": "Личный кабинет",
        "icon_class": "fas fa-child fa-fw me-1",
    },
    {
        "url": "instructor_schedule",
        "name_block": "link-body-emphasis",
        "title": "Расписание занятий",
        "icon_class": "fas fa-clipboard-list fa-fw me-1",
    },
    {
        "url": "instructor_students",
        "name_block": "link-body-emphasis",
        "title": "Ученики",
        "icon_class": "fas fa-user-graduate fa-fw me-1",
    },
    {
        "url": "instructor_reports",
        "name_block": "link-body-emphasis",
        "title": "Отчетность",
        "icon_class": "fas fa-flag fa-fw me-1",
    },
]
links_instructor_schedule = [
    {
        "url": "instructor_home",
        "name_block": "link-body-emphasis",
        "title": "Главная",
        "icon_class": "fas fa-house-user fa-fw me-1",
    },
    {
        "url": "instructor_profile",
        "name_block": "link-body-emphasis",
        "title": "Личный кабинет",
        "icon_class": "fas fa-child fa-fw me-1",
    },
    {
        "url": "instructor_schedule",
        "name_block": "active",
        "title": "Расписание занятий",
        "icon_class": "fas fa-clipboard-list fa-fw me-1",
    },
    {
        "url": "instructor_students",
        "name_block": "link-body-emphasis",
        "title": "Ученики",
        "icon_class": "fas fa-user-graduate fa-fw me-1",
    },
    {
        "url": "instructor_reports",
        "name_block": "link-body-emphasis",
        "title": "Отчетность",
        "icon_class": "fas fa-flag fa-fw me-1",
    },
]
links_instructor_students = [
    {
        "url": "instructor_home",
        "name_block": "link-body-emphasis",
        "title": "Главная",
        "icon_class": "fas fa-house-user fa-fw me-1",
    },
    {
        "url": "instructor_profile",
        "name_block": "link-body-emphasis",
        "title": "Личный кабинет",
        "icon_class": "fas fa-child fa-fw me-1",
    },
    {
        "url": "instructor_schedule",
        "name_block": "link-body-emphasis",
        "title": "Расписание занятий",
        "icon_class": "fas fa-clipboard-list fa-fw me-1",
    },
    {
        "url": "instructor_students",
        "name_block": "active",
        "title": "Ученики",
        "icon_class": "fas fa-user-graduate fa-fw me-1",
    },
    {
        "url": "instructor_reports",
        "name_block": "link-body-emphasis",
        "title": "Отчетность",
        "icon_class": "fas fa-flag fa-fw me-1",
    },
]
links_instructor_reports = [
    {
        "url": "instructor_home",
        "name_block": "link-body-emphasis",
        "title": "Главная",
        "icon_class": "fas fa-house-user fa-fw me-1",
    },
    {
        "url": "instructor_profile",
        "name_block": "link-body-emphasis",
        "title": "Личный кабинет",
        "icon_class": "fas fa-child fa-fw me-1",
    },
    {
        "url": "instructor_schedule",
        "name_block": "link-body-emphasis",
        "title": "Расписание занятий",
        "icon_class": "fas fa-clipboard-list fa-fw me-1",
    },
    {
        "url": "instructor_students",
        "name_block": "link-body-emphasis",
        "title": "Ученики",
        "icon_class": "fas fa-user-graduate fa-fw me-1",
    },
    {
        "url": "instructor_reports",
        "name_block": "active",
        "title": "Отчетность",
        "icon_class": "fas fa-flag fa-fw me-1",
    },
]


# Create your views here.
@login_required
def home(request):
    if instructor_exist(request):
        data = {"links": links_instructor_home}

        return render(request, "instructor/home.html", context=data)
    else:
        messages.error(request, f"У вас нет доступа к этой ссылке")
        return redirect("user_home")


@login_required
def schedule(request):
    if instructor_exist(request):
        data = {"links": links_instructor_schedule}

        return render(request, "instructor/dev.html", context=data)
    else:
        messages.error(request, f"У вас нет доступа к этой ссылке")
        return redirect("user_home")


@login_required
def students(request):
    if instructor_exist(request):
        data = {"links": links_instructor_students}

        return render(request, "instructor/dev.html", context=data)
    else:
        messages.error(request, f"У вас нет доступа к этой ссылке")
        return redirect("user_home")


@login_required
def reports(request):
    if instructor_exist(request):
        data = {"links": links_instructor_reports}

        return render(request, "instructor/dev.html", context=data)
    else:
        messages.error(request, f"У вас нет доступа к этой ссылке")
        return redirect("user_home")


def profile(request):
    user_data = Users.objects.get(id_user=request.user.id)
    if instructor_exist(request):
        links = {"links": links_instructor_profile}
    else:
        messages.error(request, f"У вас нет доступа к этой ссылке")
        return redirect("user_home")

    with connection.cursor() as cursor:
        cursor.execute("Select ID_category, Name from DrivingCategories")
        rows = cursor.fetchall()
        drivingcategory_data = []
        for row in rows:
            drivingcategory_data.append(row)

        query = f"Select Cars.Model, Cars.Color_auto, Cars.Reg_number_auto from Instructors join Cars on Instructors.ID_car = Cars.ID_car where ID_instructor = {request.user.id}"
        cursor.execute(query)
        row = cursor.fetchone()

        car_data = row

    user_data = {"user_data": user_data} | links
    user_data = user_data | {"drivingcategories": drivingcategory_data}
    user_data = user_data | {"car": car_data}

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

        modelcar = request.POST.get("modelcar")
        colorcar = request.POST.get("colorcar")
        reg_number_auto = request.POST.get("reg_number_auto")
        drivingcategory = request.POST.get("drivingcategory")

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

                query = f"Select ID_car from Instructors where ID_instructor = {request.user.id}"
                cursor.execute(query)
                row = cursor.fetchone()
                car_id = row[0]

                query = f"Update Instructors set ID_category = {drivingcategory} where ID_instructor = {request.user.id}"
                cursor.execute(query)

                query = "Update Cars Set Model = %s, Color_auto = %s, Reg_number_auto = %s where ID_car = %s"
                vals = (modelcar, colorcar, reg_number_auto, car_id)
                cursor.execute(query, vals)

                connection.commit()

            messages.success(request, f"Изменения успешно сохранены.")
            return redirect("instructor_profile")
        except:
            messages.error(request, f"Ошибка сохранения данных.")

    return render(request, "instructor/profile.html", context=user_data)
