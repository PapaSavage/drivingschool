from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.db import connection
from django.contrib.auth.decorators import login_required
import sys

sys.path.append(r"D:\Projects\drivingschool")
from users.models import Users
from usertype import *

# Create your views here.

links_user_tarrif = [
    {
        "url": "user_home",
        "name_block": "link-body-emphasis",
        "title": "Главная",
        "icon_class": "fas fa-house-user fa-fw me-1",
    },
    {
        "url": "profile",
        "name_block": "link-body-emphasis",
        "title": "Личный кабинет",
        "icon_class": "fas fa-child fa-fw me-1",
    },
    {
        "url": "user_tariffs",
        "name_block": "active",
        "title": "Тарифы",
        "icon_class": "fas fa-receipt fa-fw me-1",
    },
]
links_user_home = [
    {
        "url": "user_home",
        "name_block": "active",
        "title": "Главная",
        "icon_class": "fas fa-house-user fa-fw me-1",
    },
    {
        "url": "profile",
        "name_block": "link-body-emphasis",
        "title": "Личный кабинет",
        "icon_class": "fas fa-child fa-fw me-1",
    },
    {
        "url": "user_tariffs",
        "name_block": "link-body-emphasis",
        "title": "Тарифы",
        "icon_class": "fas fa-receipt fa-fw me-1",
    },
]
links_user_profile = [
    {
        "url": "user_home",
        "name_block": "link-body-emphasis",
        "title": "Главная",
        "icon_class": "fas fa-house-user fa-fw me-1",
    },
    {
        "url": "profile",
        "name_block": "active",
        "title": "Личный кабинет",
        "icon_class": "fas fa-child fa-fw me-1",
    },
    {
        "url": "user_tariffs",
        "name_block": "link-body-emphasis",
        "title": "Тарифы",
        "icon_class": "fas fa-receipt fa-fw me-1",
    },
]

links_admin_home = [
    {
        "url": "user_home",
        "name_block": "active",
        "title": "Главная",
        "icon_class": "fas fa-house-user fa-fw me-1",
    },
    {
        "url": "profile",
        "name_block": "link-body-emphasis",
        "title": "Личный кабинет",
        "icon_class": "fas fa-child fa-fw me-1",
    },
]
links_admin_profile = [
    {
        "url": "user_home",
        "name_block": "link-body-emphasis",
        "title": "Главная",
        "icon_class": "fas fa-house-user fa-fw me-1",
    },
    {
        "url": "profile",
        "name_block": "active",
        "title": "Личный кабинет",
        "icon_class": "fas fa-child fa-fw me-1",
    },
]
links_lecture_home = [
    {
        "url": "user_home",
        "name_block": "active",
        "title": "Главная",
        "icon_class": "fas fa-house-user fa-fw me-1",
    },
    {
        "url": "profile",
        "name_block": "link-body-emphasis",
        "title": "Личный кабинет",
        "icon_class": "fas fa-child fa-fw me-1",
    },
]
links_lecture_profile = [
    {
        "url": "user_home",
        "name_block": "link-body-emphasis",
        "title": "Главная",
        "icon_class": "fas fa-house-user fa-fw me-1",
    },
    {
        "url": "profile",
        "name_block": "active",
        "title": "Личный кабинет",
        "icon_class": "fas fa-child fa-fw me-1",
    },
]
links_instructor_home = [
    {
        "url": "user_home",
        "name_block": "active",
        "title": "Главная",
        "icon_class": "fas fa-house-user fa-fw me-1",
    },
    {
        "url": "profile",
        "name_block": "link-body-emphasis",
        "title": "Личный кабинет",
        "icon_class": "fas fa-child fa-fw me-1",
    },
]
links_instructor_profile = [
    {
        "url": "user_home",
        "name_block": "link-body-emphasis",
        "title": "Главная",
        "icon_class": "fas fa-house-user fa-fw me-1",
    },
    {
        "url": "profile",
        "name_block": "active",
        "title": "Личный кабинет",
        "icon_class": "fas fa-child fa-fw me-1",
    },
]
links_student_home = [
    {
        "url": "user_home",
        "name_block": "active",
        "title": "Главная",
        "icon_class": "fas fa-house-user fa-fw me-1",
    },
    {
        "url": "profile",
        "name_block": "link-body-emphasis",
        "title": "Личный кабинет",
        "icon_class": "fas fa-child fa-fw me-1",
    },
]
links_student_profile = [
    {
        "url": "user_home",
        "name_block": "link-body-emphasis",
        "title": "Главная",
        "icon_class": "fas fa-house-user fa-fw me-1",
    },
    {
        "url": "profile",
        "name_block": "active",
        "title": "Личный кабинет",
        "icon_class": "fas fa-child fa-fw me-1",
    },
]


def check_user_reg(request):
    with connection.cursor() as cursor:
        cursor.execute(
            "Select Surname from Users where ID_user = %s", (request.user.id,)
        )
        row = cursor.fetchone()

    if row[0]:
        return True
    else:
        return False


@login_required
def home(request):
    if admin_exist(request):
        return redirect("admin_home")

    elif instructor_exist(request):
        return redirect("instructor_home")

    elif lecture_exist(request):
        return redirect("lector_home")

    elif student_exist(request):
        return redirect("student_home")

    else:
        links = {"links": links_user_home}
        if not check_user_reg(request):
            messages.info(request, f"Введите свои данные.")
            return redirect("profile")
        elif not student_exist(request):
            messages.info(request, f"Выберите учебный план")
            return redirect("user_tariffs")

    data = links

    return render(request, "users/home.html", context=data)


@login_required
def user_tariffs(request):
    if admin_exist(request):
        messages.info(request, f"Вы являетесь администратором.")
        return redirect("admin_home")

    elif instructor_exist(request):
        messages.info(request, f"Вы являетесь инструктором.")
        return redirect("instructor_home")

    elif lecture_exist(request):
        messages.info(request, f"Вы являетесь лектором.")
        return redirect("lecture_home")

    elif student_exist(request):
        messages.info(request, f"Вы уже являетесь студентом.")
        return redirect("student_home")

    else:
        if not check_user_reg(request):
            messages.info(request, f"Введите свои данные.")
            return redirect("profile")

        else:
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
                data = data | {"links": links_user_tarrif}
            if request.method == "POST":
                idplan = request.POST.get("idplan")
                try:
                    with connection.cursor() as cursor:
                        query = f"Insert IGNORE into Students (ID_student) values ({request.user.id})"
                        cursor.execute(query)

                        query = """SELECT g.ID_group, g.Name
FROM Groupes g
LEFT JOIN Contracts c ON g.ID_group = c.ID_group
where c.ID_plan = %s
GROUP BY g.ID_group, g.Name
HAVING COUNT(c.ID_contract) < 20
ORDER BY g.ID_group;"""
                        vals = (idplan,)

                        cursor.execute(query, vals)
                        row = cursor.fetchone()
                        if row:
                            idgroup = row[0]
                        else:
                            query = f"""SELECT Lectures.ID_lecture 
        FROM Lectures 
        LEFT JOIN Groupes ON Groupes.ID_lecture = Lectures.ID_lecture 
        GROUP BY ID_lecture 
        ORDER BY COUNT(*) 
        LIMIT 1"""
                            cursor.execute(query)
                            ID_lecture = cursor.fetchone()[0]
                            query = f"""SELECT Lectures.ID_lecture 
        FROM Lectures 
        LEFT JOIN Groupes ON Groupes.ID_lecture = Lectures.ID_lecture 
        GROUP BY ID_lecture 
        ORDER BY COUNT(*) 
        LIMIT 1"""
                            cursor.execute(query)
                            group_name = cursor.fetchone()[0]

                            query = (
                                "INSERT INTO Groupes (ID_lecture, Name) Values (%s, %s)"
                            )
                            vals = (ID_lecture, group_name)
                            cursor.execute(query, vals)

                            query = "SELECT ID_group FROM Groupes ORDER by ID_group desc limit 1"
                            cursor.execute(query)

                            row = cursor.fetchone()

                            idgroup = row[0]

                        query = "SELECT DrivingCategories.ID_category FROM DrivingCategories JOIN PlansEducations ON DrivingCategories.ID_category = PlansEducations.ID_category WHERE PlansEducations.ID_plan = 4;"
                        cursor.execute(query)
                        drivingcategory = cursor.fetchone()[0]

                        query = f"Select Instructors.ID_instructor, Count(*) as quantity from Instructors LEFT JOIN Contracts on Instructors.ID_instructor = Contracts.ID_instructor where Instructors.ID_instructor in (Select ID_instructor from Instructors where ID_category = {drivingcategory}) GROUP by ID_instructor ORDER by quantity ASC Limit 1"
                        cursor.execute(query)
                        instructor_id = cursor.fetchone()[0]

                        query = "Insert into Contracts (DateContractStart, ID_group, ID_instructor, ID_student, ID_plan) values (NOW(), %s, %s, %s, %s)"
                        vals = (idgroup, instructor_id, request.user.id, idplan)
                        cursor.execute(query, vals)

                        connection.commit()

                        messages.success(request, f"Добро пожаловать в автошколу!")
                    return redirect("student_home")

                except:
                    messages.error(request, f"Ошибка при работе с базой данных.")

    return render(request, "users/tariffs.html", context=data)


@login_required
def profile(request):
    user_data = Users.objects.get(id_user=request.user.id)
    if admin_exist(request):
        return redirect("admin_profile")

    elif instructor_exist(request):
        return redirect("instructor_profile")

    elif lecture_exist(request):
        return redirect("lecture_profile")

    elif student_exist(request):
        return redirect("student_profile")

    else:
        links = {"links": links_user_profile}
        if check_user_reg(request):
            if not student_exist(request):
                messages.info(request, f"Выберите учебный план")
                return redirect("user_tariffs")

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
            if check_user_reg(request):
                if not student_exist(request):
                    return redirect("user_home")
        except:
            messages.error(request, f"Ошибка сохранения данных.")

    return render(request, "users/profile.html", context=user_data)
