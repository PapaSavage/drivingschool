from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.db import connection
from django.contrib.auth.decorators import login_required
import sys

sys.path.append(r"D:\Projects\drivingschool")
from users.models import Users
from usertype import *


links_student_home = [
    {
        "url": "student_home",
        "name_block": "active",
        "title": "Главная",
        "icon_class": "fas fa-house-user fa-fw me-1",
    },
    {
        "url": "student_profile",
        "name_block": "link-body-emphasis",
        "title": "Личный кабинет",
        "icon_class": "fas fa-child fa-fw me-1",
    },
    {
        "url": "student_study",
        "name_block": "link-body-emphasis",
        "title": "Учебные материалы",
        "icon_class": "fas fa-school fa-fw me-1",
    },
    {
        "url": "student_schedule",
        "name_block": "link-body-emphasis",
        "title": "Расписание занятий",
        "icon_class": "fas fa-clipboard-list fa-fw me-1",
    },
    {
        "url": "student_tests",
        "name_block": "link-body-emphasis",
        "title": "Тесты",
        "icon_class": "fas fa-question fa-fw me-1",
    },
    {
        "url": "student_exams",
        "name_block": "link-body-emphasis",
        "title": "Экзамены",
        "icon_class": "fas fa-school fa-fw me-1",
    },
    {
        "url": "student_messages",
        "name_block": "link-body-emphasis",
        "title": "Сообщения",
        "icon_class": "fas fa-comments fa-fw me-1",
    },
]
links_student_profile = [
    {
        "url": "student_home",
        "name_block": "link-body-emphasis",
        "title": "Главная",
        "icon_class": "fas fa-house-user fa-fw me-1",
    },
    {
        "url": "student_profile",
        "name_block": "active",
        "title": "Личный кабинет",
        "icon_class": "fas fa-child fa-fw me-1",
    },
    {
        "url": "student_study",
        "name_block": "link-body-emphasis",
        "title": "Учебные материалы",
        "icon_class": "fas fa-school fa-fw me-1",
    },
    {
        "url": "student_schedule",
        "name_block": "link-body-emphasis",
        "title": "Расписание занятий",
        "icon_class": "fas fa-clipboard-list fa-fw me-1",
    },
    {
        "url": "student_tests",
        "name_block": "link-body-emphasis",
        "title": "Тесты",
        "icon_class": "fas fa-question fa-fw me-1",
    },
    {
        "url": "student_exams",
        "name_block": "link-body-emphasis",
        "title": "Экзамены",
        "icon_class": "fas fa-school fa-fw me-1",
    },
    {
        "url": "student_messages",
        "name_block": "link-body-emphasis",
        "title": "Сообщения",
        "icon_class": "fas fa-comments fa-fw me-1",
    },
]
links_student_study = [
    {
        "url": "student_home",
        "name_block": "link-body-emphasis",
        "title": "Главная",
        "icon_class": "fas fa-house-user fa-fw me-1",
    },
    {
        "url": "student_profile",
        "name_block": "link-body-emphasis",
        "title": "Личный кабинет",
        "icon_class": "fas fa-child fa-fw me-1",
    },
    {
        "url": "student_study",
        "name_block": "active",
        "title": "Учебные материалы",
        "icon_class": "fas fa-school fa-fw me-1",
    },
    {
        "url": "student_schedule",
        "name_block": "link-body-emphasis",
        "title": "Расписание занятий",
        "icon_class": "fas fa-clipboard-list fa-fw me-1",
    },
    {
        "url": "student_tests",
        "name_block": "link-body-emphasis",
        "title": "Тесты",
        "icon_class": "fas fa-question fa-fw me-1",
    },
    {
        "url": "student_exams",
        "name_block": "link-body-emphasis",
        "title": "Экзамены",
        "icon_class": "fas fa-school fa-fw me-1",
    },
    {
        "url": "student_messages",
        "name_block": "link-body-emphasis",
        "title": "Сообщения",
        "icon_class": "fas fa-comments fa-fw me-1",
    },
]
links_student_schedule = [
    {
        "url": "student_home",
        "name_block": "link-body-emphasis",
        "title": "Главная",
        "icon_class": "fas fa-house-user fa-fw me-1",
    },
    {
        "url": "student_profile",
        "name_block": "link-body-emphasis",
        "title": "Личный кабинет",
        "icon_class": "fas fa-child fa-fw me-1",
    },
    {
        "url": "student_study",
        "name_block": "link-body-emphasis",
        "title": "Учебные материалы",
        "icon_class": "fas fa-school fa-fw me-1",
    },
    {
        "url": "student_schedule",
        "name_block": "active",
        "title": "Расписание занятий",
        "icon_class": "fas fa-clipboard-list fa-fw me-1",
    },
    {
        "url": "student_tests",
        "name_block": "link-body-emphasis",
        "title": "Тесты",
        "icon_class": "fas fa-question fa-fw me-1",
    },
    {
        "url": "student_exams",
        "name_block": "link-body-emphasis",
        "title": "Экзамены",
        "icon_class": "fas fa-school fa-fw me-1",
    },
    {
        "url": "student_messages",
        "name_block": "link-body-emphasis",
        "title": "Сообщения",
        "icon_class": "fas fa-comments fa-fw me-1",
    },
]
links_student_tests = [
    {
        "url": "student_home",
        "name_block": "link-body-emphasis",
        "title": "Главная",
        "icon_class": "fas fa-house-user fa-fw me-1",
    },
    {
        "url": "student_profile",
        "name_block": "link-body-emphasis",
        "title": "Личный кабинет",
        "icon_class": "fas fa-child fa-fw me-1",
    },
    {
        "url": "student_study",
        "name_block": "link-body-emphasis",
        "title": "Учебные материалы",
        "icon_class": "fas fa-school fa-fw me-1",
    },
    {
        "url": "student_schedule",
        "name_block": "link-body-emphasis",
        "title": "Расписание занятий",
        "icon_class": "fas fa-clipboard-list fa-fw me-1",
    },
    {
        "url": "student_tests",
        "name_block": "active",
        "title": "Тесты",
        "icon_class": "fas fa-question fa-fw me-1",
    },
    {
        "url": "student_exams",
        "name_block": "link-body-emphasis",
        "title": "Экзамены",
        "icon_class": "fas fa-school fa-fw me-1",
    },
    {
        "url": "student_messages",
        "name_block": "link-body-emphasis",
        "title": "Сообщения",
        "icon_class": "fas fa-comments fa-fw me-1",
    },
]
links_student_exams = [
    {
        "url": "student_home",
        "name_block": "link-body-emphasis",
        "title": "Главная",
        "icon_class": "fas fa-house-user fa-fw me-1",
    },
    {
        "url": "student_profile",
        "name_block": "link-body-emphasis",
        "title": "Личный кабинет",
        "icon_class": "fas fa-child fa-fw me-1",
    },
    {
        "url": "student_study",
        "name_block": "link-body-emphasis",
        "title": "Учебные материалы",
        "icon_class": "fas fa-school fa-fw me-1",
    },
    {
        "url": "student_schedule",
        "name_block": "link-body-emphasis",
        "title": "Расписание занятий",
        "icon_class": "fas fa-clipboard-list fa-fw me-1",
    },
    {
        "url": "student_tests",
        "name_block": "link-body-emphasis",
        "title": "Тесты",
        "icon_class": "fas fa-question fa-fw me-1",
    },
    {
        "url": "student_exams",
        "name_block": "active",
        "title": "Экзамены",
        "icon_class": "fas fa-school fa-fw me-1",
    },
    {
        "url": "student_messages",
        "name_block": "link-body-emphasis",
        "title": "Сообщения",
        "icon_class": "fas fa-comments fa-fw me-1",
    },
]
links_student_messages = [
    {
        "url": "student_home",
        "name_block": "link-body-emphasis",
        "title": "Главная",
        "icon_class": "fas fa-house-user fa-fw me-1",
    },
    {
        "url": "student_profile",
        "name_block": "link-body-emphasis",
        "title": "Личный кабинет",
        "icon_class": "fas fa-child fa-fw me-1",
    },
    {
        "url": "student_study",
        "name_block": "link-body-emphasis",
        "title": "Учебные материалы",
        "icon_class": "fas fa-school fa-fw me-1",
    },
    {
        "url": "student_schedule",
        "name_block": "link-body-emphasis",
        "title": "Расписание занятий",
        "icon_class": "fas fa-clipboard-list fa-fw me-1",
    },
    {
        "url": "student_tests",
        "name_block": "link-body-emphasis",
        "title": "Тесты",
        "icon_class": "fas fa-question fa-fw me-1",
    },
    {
        "url": "student_exams",
        "name_block": "link-body-emphasis",
        "title": "Экзамены",
        "icon_class": "fas fa-school fa-fw me-1",
    },
    {
        "url": "student_messages",
        "name_block": "active",
        "title": "Сообщения",
        "icon_class": "fas fa-comments fa-fw me-1",
    },
]


# Create your views here.
@login_required
def home(request):
    if student_exist(request):
        data = {"links": links_student_home}

        return render(request, "student/home.html", context=data)
    else:
        messages.error(request, f"У вас нет доступа к этой ссылке")
        return redirect("user_home")


@login_required
def study(request):
    if student_exist(request):
        data = {"links": links_student_study}

        return render(request, "student/dev.html", context=data)
    else:
        messages.error(request, f"У вас нет доступа к этой ссылке")
        return redirect("user_home")


@login_required
def schedule(request):
    if student_exist(request):
        data = {"links": links_student_schedule}

        return render(request, "student/dev.html", context=data)
    else:
        messages.error(request, f"У вас нет доступа к этой ссылке")
        return redirect("user_home")


@login_required
def tests(request):
    if student_exist(request):
        data = {"links": links_student_tests}

        return render(request, "student/dev.html", context=data)
    else:
        messages.error(request, f"У вас нет доступа к этой ссылке")
        return redirect("user_home")


@login_required
def exams(request):
    if student_exist(request):
        data = {"links": links_student_exams}

        if request.method == "POST":
            insightpassexam = request.POST.get("insightpassexam")
            outsidepassexam = request.POST.get("outsidepassexam")

            if insightpassexam:
                with connection.cursor() as cursor:
                    query = f"UPDATE Students Set InsightPassExam = 1 where ID_student = {request.user.id}"
                    cursor.execute(query)
                    messages.success(request, f"Внутренний экзамен был успешно сдан!")
            elif outsidepassexam:
                with connection.cursor() as cursor:
                    query = f"UPDATE Students Set OutsidePassExam = 1 where ID_student = {request.user.id}"
                    cursor.execute(query)
                    messages.success(request, f"Внешний экзамен был успешно сдан!")

        return render(request, "student/exams.html", context=data)
    else:
        messages.error(request, f"У вас нет доступа к этой ссылке")
        return redirect("user_home")


@login_required
def message(request):
    if student_exist(request):
        data = {"links": links_student_messages}

        return render(request, "student/dev.html", context=data)
    else:
        messages.error(request, f"У вас нет доступа к этой ссылке")
        return redirect("user_home")


def profile(request):
    user_data = Users.objects.get(id_user=request.user.id)
    if student_exist(request):
        links = {"links": links_student_profile}
    else:
        messages.error(request, f"У вас нет доступа к этой ссылке")
        return redirect("user_home")

    with connection.cursor() as cursor:
        cursor.execute(
            f"Select DrivingCategories.Name from DrivingCategories join PlansEducations on DrivingCategories.ID_category = PlansEducations.ID_category join Contracts on PlansEducations.ID_plan = Contracts.ID_plan where Contracts.ID_student = {request.user.id}"
        )
        drivingcategory = cursor.fetchone()[0]

        cursor.execute(
            f"Select CONCAT(Users.Surname, ' ', Users.Name, ' ', Users.SecondName) as InstructorFIO from Instructors join Contracts on Contracts.ID_instructor = Instructors.ID_instructor join Users on Users.ID_user = Instructors.ID_instructor where Contracts.ID_student = {request.user.id}"
        )
        inst_fio = cursor.fetchone()
        print(inst_fio)

    user_data = (
        {"user_data": user_data}
        | links
        | {"drivingcategory": drivingcategory}
        | {"inst_fio": inst_fio}
    )

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
            return redirect("student_profile")
        except:
            messages.error(request, f"Ошибка сохранения данных.")

    return render(request, "student/profile.html", context=user_data)
