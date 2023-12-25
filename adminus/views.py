from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.db import connection
from django.contrib.auth.decorators import login_required
import sys
from django.contrib.auth.models import User
from users.models import Users
from usertype import *

sys.path.append(r"D:\Projects\drivingschool")

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
    {
        "url": "admin_lectures",
        "name_block": "link-body-emphasis",
        "title": "Лекторы",
        "icon_class": "fas fa-chalkboard-teacher fa-fw me-1",
    },
    {
        "url": "admin_students",
        "name_block": "link-body-emphasis",
        "title": "Студенты",
        "icon_class": "fas fa-user-graduate fa-fw me-1",
    },
    {
        "url": "admin_groups",
        "name_block": "link-body-emphasis",
        "title": "Группы",
        "icon_class": "fas fa-users fa-fw me-1",
    },
    {
        "url": "admin_reports",
        "name_block": "link-body-emphasis",
        "title": "Отчёты",
        "icon_class": "fas fa-flag fa-fw me-1",
    },
    {
        "url": "admin_money",
        "name_block": "link-body-emphasis",
        "title": "Финансы",
        "icon_class": "fas fa-money-bill-alt fa-fw me-1",
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
    {
        "url": "admin_lectures",
        "name_block": "link-body-emphasis",
        "title": "Лекторы",
        "icon_class": "fas fa-chalkboard-teacher fa-fw me-1",
    },
    {
        "url": "admin_students",
        "name_block": "link-body-emphasis",
        "title": "Студенты",
        "icon_class": "fas fa-user-graduate fa-fw me-1",
    },
    {
        "url": "admin_groups",
        "name_block": "link-body-emphasis",
        "title": "Группы",
        "icon_class": "fas fa-users fa-fw me-1",
    },
    {
        "url": "admin_reports",
        "name_block": "link-body-emphasis",
        "title": "Отчёты",
        "icon_class": "fas fa-flag fa-fw me-1",
    },
    {
        "url": "admin_money",
        "name_block": "link-body-emphasis",
        "title": "Финансы",
        "icon_class": "fas fa-money-bill-alt fa-fw me-1",
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
    {
        "url": "admin_lectures",
        "name_block": "link-body-emphasis",
        "title": "Лекторы",
        "icon_class": "fas fa-chalkboard-teacher fa-fw me-1",
    },
    {
        "url": "admin_students",
        "name_block": "link-body-emphasis",
        "title": "Студенты",
        "icon_class": "fas fa-user-graduate fa-fw me-1",
    },
    {
        "url": "admin_groups",
        "name_block": "link-body-emphasis",
        "title": "Группы",
        "icon_class": "fas fa-users fa-fw me-1",
    },
    {
        "url": "admin_reports",
        "name_block": "link-body-emphasis",
        "title": "Отчёты",
        "icon_class": "fas fa-flag fa-fw me-1",
    },
    {
        "url": "admin_money",
        "name_block": "link-body-emphasis",
        "title": "Финансы",
        "icon_class": "fas fa-money-bill-alt fa-fw me-1",
    },
]
links_admin_lectures = [
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
        "name_block": "link-body-emphasis",
        "title": "Инструкторы",
        "icon_class": "fas fa-biking fa-fw me-1",
    },
    {
        "url": "admin_lectures",
        "name_block": "active",
        "title": "Лекторы",
        "icon_class": "fas fa-chalkboard-teacher fa-fw me-1",
    },
    {
        "url": "admin_students",
        "name_block": "link-body-emphasis",
        "title": "Студенты",
        "icon_class": "fas fa-user-graduate fa-fw me-1",
    },
    {
        "url": "admin_groups",
        "name_block": "link-body-emphasis",
        "title": "Группы",
        "icon_class": "fas fa-users fa-fw me-1",
    },
    {
        "url": "admin_reports",
        "name_block": "link-body-emphasis",
        "title": "Отчёты",
        "icon_class": "fas fa-flag fa-fw me-1",
    },
    {
        "url": "admin_money",
        "name_block": "link-body-emphasis",
        "title": "Финансы",
        "icon_class": "fas fa-money-bill-alt fa-fw me-1",
    },
]
links_admin_students = [
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
        "name_block": "link-body-emphasis",
        "title": "Инструкторы",
        "icon_class": "fas fa-biking fa-fw me-1",
    },
    {
        "url": "admin_lectures",
        "name_block": "link-body-emphasis",
        "title": "Лекторы",
        "icon_class": "fas fa-chalkboard-teacher fa-fw me-1",
    },
    {
        "url": "admin_students",
        "name_block": "active",
        "title": "Студенты",
        "icon_class": "fas fa-user-graduate fa-fw me-1",
    },
    {
        "url": "admin_groups",
        "name_block": "link-body-emphasis",
        "title": "Группы",
        "icon_class": "fas fa-users fa-fw me-1",
    },
    {
        "url": "admin_reports",
        "name_block": "link-body-emphasis",
        "title": "Отчёты",
        "icon_class": "fas fa-flag fa-fw me-1",
    },
    {
        "url": "admin_money",
        "name_block": "link-body-emphasis",
        "title": "Финансы",
        "icon_class": "fas fa-money-bill-alt fa-fw me-1",
    },
]
links_admin_reports = [
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
        "name_block": "link-body-emphasis",
        "title": "Инструкторы",
        "icon_class": "fas fa-biking fa-fw me-1",
    },
    {
        "url": "admin_lectures",
        "name_block": "link-body-emphasis",
        "title": "Лекторы",
        "icon_class": "fas fa-chalkboard-teacher fa-fw me-1",
    },
    {
        "url": "admin_students",
        "name_block": "link-body-emphasis",
        "title": "Студенты",
        "icon_class": "fas fa-user-graduate fa-fw me-1",
    },
    {
        "url": "admin_groups",
        "name_block": "link-body-emphasis",
        "title": "Группы",
        "icon_class": "fas fa-users fa-fw me-1",
    },
    {
        "url": "admin_reports",
        "name_block": "active",
        "title": "Отчёты",
        "icon_class": "fas fa-flag fa-fw me-1",
    },
    {
        "url": "admin_money",
        "name_block": "link-body-emphasis",
        "title": "Финансы",
        "icon_class": "fas fa-money-bill-alt fa-fw me-1",
    },
]
links_admin_groups = [
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
        "name_block": "link-body-emphasis",
        "title": "Инструкторы",
        "icon_class": "fas fa-biking fa-fw me-1",
    },
    {
        "url": "admin_lectures",
        "name_block": "link-body-emphasis",
        "title": "Лекторы",
        "icon_class": "fas fa-chalkboard-teacher fa-fw me-1",
    },
    {
        "url": "admin_students",
        "name_block": "link-body-emphasis",
        "title": "Студенты",
        "icon_class": "fas fa-user-graduate fa-fw me-1",
    },
    {
        "url": "admin_groups",
        "name_block": "active",
        "title": "Группы",
        "icon_class": "fas fa-users fa-fw me-1",
    },
    {
        "url": "admin_reports",
        "name_block": "link-body-emphasis",
        "title": "Отчёты",
        "icon_class": "fas fa-flag fa-fw me-1",
    },
    {
        "url": "admin_money",
        "name_block": "link-body-emphasis",
        "title": "Финансы",
        "icon_class": "fas fa-money-bill-alt fa-fw me-1",
    },
]
links_admin_money = [
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
        "name_block": "link-body-emphasis",
        "title": "Инструкторы",
        "icon_class": "fas fa-biking fa-fw me-1",
    },
    {
        "url": "admin_lectures",
        "name_block": "link-body-emphasis",
        "title": "Лекторы",
        "icon_class": "fas fa-chalkboard-teacher fa-fw me-1",
    },
    {
        "url": "admin_students",
        "name_block": "link-body-emphasis",
        "title": "Студенты",
        "icon_class": "fas fa-user-graduate fa-fw me-1",
    },
    {
        "url": "admin_groups",
        "name_block": "link-body-emphasis",
        "title": "Группы",
        "icon_class": "fas fa-users fa-fw me-1",
    },
    {
        "url": "admin_reports",
        "name_block": "link-body-emphasis",
        "title": "Отчёты",
        "icon_class": "fas fa-flag fa-fw me-1",
    },
    {
        "url": "admin_money",
        "name_block": "active",
        "title": "Финансы",
        "icon_class": "fas fa-money-bill-alt fa-fw me-1",
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
def groups(request):
    if admin_exist(request):
        data = {"links": links_admin_groups}

        return render(request, "adminus/groups.html", context=data)
    else:
        messages.error(request, f"У вас нет доступа к этой ссылке")
        return redirect("user_home")


@login_required
def reports(request):
    if admin_exist(request):
        data = {"links": links_admin_reports}

        return render(request, "adminus/dev.html", context=data)
    else:
        messages.error(request, f"У вас нет доступа к этой ссылке")
        return redirect("user_home")


@login_required
def money(request):
    if admin_exist(request):
        data = {"links": links_admin_money}

        return render(request, "adminus/dev.html", context=data)
    else:
        messages.error(request, f"У вас нет доступа к этой ссылке")
        return redirect("user_home")


@login_required
def instructors(request):
    if admin_exist(request):
        data = {"links": links_admin_instructors}

        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT Users.ID_user, CONCAT(Users.Surname, ' ', Users.Name, ' ', Users.SecondName) as FIO, Users.Telephone as Telephone, Cars.Model as Model, Users.Surname, Users.Name, Users.SecondName, Users.Adress, Users.DateOfBirth, Users.Passport, Users.SeriaMedicalCertificate, Users.Email, Cars.Color_auto, Cars.Reg_number_auto, DrivingCategories.Name FROM Instructors JOIN Users on Instructors.ID_instructor = Users.ID_user LEFT JOIN Cars on Instructors.ID_car = Cars.ID_car left JOIN DrivingCategories on Instructors.ID_category = DrivingCategories.ID_category"
            )
            rows = cursor.fetchall()
            instructors_data = []
            for row in rows:
                instructors_data.append(row)
            cursor.execute("Select Count(*) from Instructors")
            row = cursor.fetchone()
            count = row[0]

            cursor.execute("Select ID_category, Name from DrivingCategories")
            rows = cursor.fetchall()
            drivingcategory_data = []
            for row in rows:
                drivingcategory_data.append(row)

            instruct = {
                "instructors": instructors_data,
                "count": count,
                "drivingcategories": drivingcategory_data,
            }

        data = data | instruct

        if request.method == "POST":
            login = request.POST.get("login")
            password = request.POST.get("password")

            inst_id = request.POST.get("inst_id")

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
            delcheck = request.POST.get("del")

            if delcheck:
                user_to_delete = User.objects.get(id=inst_id)

                # Удалите пользователя
                user_to_delete.delete()
                messages.success(request, f"Изменения успешно сохранены.")
                return redirect("admin_instructors")

            if login:
                user = User.objects.create_user(login, email, password)
                user.save()

            try:
                with connection.cursor() as cursor:
                    if login:
                        query = "SELECT id FROM auth_user order by id desc limit 1"
                        cursor.execute(query)
                        row = cursor.fetchone()
                        inst_id = row[0]

                        vals = (modelcar, colorcar, reg_number_auto)
                        query = "Insert into Cars (Model, Color_auto, Reg_number_auto) VALUES (%s, %s, %s)"
                        cursor.execute(query, vals)

                        query = "SELECT ID_car FROM Cars order by ID_car desc limit 1"
                        cursor.execute(query)
                        row = cursor.fetchone()
                        car_id = row[0]

                        query = f"Insert into Instructors (ID_instructor, ID_car, ID_category) VALUES ({inst_id}, {car_id}, {drivingcategory})"
                        cursor.execute(query)

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
                        inst_id,
                    )
                    cursor.execute(query, vals)

                    query = f"Select ID_car from Instructors where ID_instructor = {inst_id}"
                    cursor.execute(query)
                    row = cursor.fetchone()
                    car_id = row[0]

                    query = f"Update Instructors set ID_category = {drivingcategory} where ID_instructor = {inst_id}"
                    cursor.execute(query)

                    query = "Update Cars Set Model = %s, Color_auto = %s, Reg_number_auto = %s where ID_car = %s"
                    vals = (modelcar, colorcar, reg_number_auto, car_id)
                    cursor.execute(query, vals)

                    connection.commit()
                messages.success(request, f"Изменения успешно сохранены.")
                return redirect("admin_instructors")
            except:
                messages.error(request, f"Ошибка сохранения данных.")

        return render(request, "adminus/instructors.html", context=data)
    else:
        messages.error(request, f"У вас нет доступа к этой ссылке")
        return redirect("user_home")


@login_required
def lectures(request):
    if admin_exist(request):
        data = {"links": links_admin_lectures}

        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT Users.ID_user, CONCAT(Users.Surname, ' ', Users.Name, ' ', Users.SecondName) as FIO, Users.Telephone as Telephone, Users.Surname, Users.Name, Users.SecondName, Users.Adress, Users.DateOfBirth, Users.Passport, Users.SeriaMedicalCertificate, Users.Email FROM Lectures JOIN Users on Lectures.ID_lecture = Users.ID_user"
            )
            rows = cursor.fetchall()
            lectures_data = []
            for row in rows:
                lectures_data.append(row)
            cursor.execute("Select Count(*) from Lectures")
            row = cursor.fetchone()
            count = row[0]
            lectr = {
                "lectures": lectures_data,
                "count": count,
            }

        data = data | lectr

        if request.method == "POST":
            login = request.POST.get("login")
            password = request.POST.get("password")

            lect_id = request.POST.get("lect_id")

            surname = request.POST.get("surname")
            firstname = request.POST.get("firstname")
            secondname = request.POST.get("secondname")
            adress = request.POST.get("adress")
            phone = request.POST.get("phone")
            date = request.POST.get("date")
            passport = request.POST.get("passport")
            medicalcertificate = request.POST.get("medicalcertificate")
            email = request.POST.get("email")

            delcheck = request.POST.get("del")

            if delcheck:
                user_to_delete = User.objects.get(id=lect_id)
                user_to_delete.delete()
                messages.success(request, f"Изменения успешно сохранены.")
                return redirect("admin_lectures")

            if login:
                user = User.objects.create_user(login, email, password)
                user.save()

            try:
                with connection.cursor() as cursor:
                    if login:
                        query = "SELECT id FROM auth_user order by id desc limit 1"
                        cursor.execute(query)
                        row = cursor.fetchone()
                        lect_id = row[0]

                        query = f"Insert into Lectures (ID_lecture) VALUES ({lect_id})"
                        cursor.execute(query)

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
                        lect_id,
                    )
                    cursor.execute(query, vals)
                    connection.commit()
                messages.success(request, f"Изменения успешно сохранены.")
                return redirect("admin_lectures")
            except:
                messages.error(request, f"Ошибка сохранения данных.")

        return render(request, "adminus/lectures.html", context=data)
    else:
        messages.error(request, f"У вас нет доступа к этой ссылке")
        return redirect("user_home")


@login_required
def students(request):
    if admin_exist(request):
        data = {"links": links_admin_students}

        with connection.cursor() as cursor:
            cursor.execute(
                """SELECT 
    Users.ID_user, 
    CONCAT(Users.Surname, ' ', Users.Name, ' ', Users.SecondName) as FIO, 
    Users.Telephone as Telephone, 
    Groupes.Name as GroupName, 
    DrivingCategories.Name as CategoryName, 
    PlansEducations.Name as EducationPlan, 
    Cars.Model,
    CONCAT(InstructorUsers.Surname, ' ', InstructorUsers.Name, ' ', InstructorUsers.SecondName) as InstructorFIO,
    Users.Surname,
    Users.Name,
    Users.SecondName,
    Users.Adress,
    Users.Telephone,
    Users.DateOfBirth,
    Users.Passport,
    Users.SeriaMedicalCertificate,
    Users.email
FROM 
    Students 
LEFT JOIN Users ON Students.ID_student = Users.ID_user 
LEFT JOIN Contracts ON Students.ID_student = Contracts.ID_student 
LEFT JOIN Groupes ON Contracts.ID_group = Groupes.ID_group 
LEFT JOIN PlansEducations ON Contracts.ID_plan = PlansEducations.ID_plan 
LEFT JOIN DrivingCategories ON PlansEducations.ID_category = DrivingCategories.ID_category 
LEFT JOIN Instructors ON Instructors.ID_instructor = Contracts.ID_instructor 
LEFT JOIN Cars ON Instructors.ID_car = Cars.ID_car
LEFT JOIN Users AS InstructorUsers ON Instructors.ID_instructor = InstructorUsers.ID_user;
"""
            )
            rows = cursor.fetchall()
            students_data = []
            for row in rows:
                students_data.append(row)

            cursor.execute("Select Count(*) from Students")
            row = cursor.fetchone()
            count = row[0]

            cursor.execute(
                "Select Instructors.ID_Instructor, CONCAT(Users.Surname, ' ', Users.Name, ' ', Users.SecondName) as InstructorFIO from Instructors join Users on Instructors.ID_instructor = Users.ID_user;"
            )

            rows = cursor.fetchall()
            instructors_data = []
            for row in rows:
                instructors_data.append(row)

            studs = {
                "students": students_data,
                "count": count,
                "instructors": instructors_data,
            }

        data = data | studs

        if request.method == "POST":
            login = request.POST.get("login")
            password = request.POST.get("password")

            stud_id = request.POST.get("stud_id")

            surname = request.POST.get("surname")
            firstname = request.POST.get("firstname")
            secondname = request.POST.get("secondname")
            adress = request.POST.get("adress")
            phone = request.POST.get("phone")
            date = request.POST.get("date")
            passport = request.POST.get("passport")
            medicalcertificate = request.POST.get("medicalcertificate")
            email = request.POST.get("email")

            inst_id = request.POST.get("inst_id")
            delcheck = request.POST.get("del")

            if delcheck:
                user_to_delete = User.objects.get(id=stud_id)
                user_to_delete.delete()
                messages.success(request, f"Изменения успешно сохранены.")
                return redirect("admin_lectures")

            if login:
                user = User.objects.create_user(login, email, password)
                user.save()

            try:
                with connection.cursor() as cursor:
                    if login:
                        query = "SELECT id FROM auth_user order by id desc limit 1"
                        cursor.execute(query)
                        row = cursor.fetchone()
                        stud_id = row[0]

                        query = f"Insert into Students (ID_student) VALUES ({stud_id})"
                        cursor.execute(query)

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
                        stud_id,
                    )
                    cursor.execute(query, vals)

                    query = (
                        "Update Contracts SET ID_instructor = %s WHERE ID_student = %s"
                    )
                    vals = (inst_id, stud_id)
                    cursor.execute(query, vals)

                    print(stud_id)

                    connection.commit()
                messages.success(request, f"Изменения успешно сохранены.")
                return redirect("admin_students")
            except:
                messages.error(request, f"Ошибка сохранения данных.")

        return render(request, "adminus/students.html", context=data)
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
            return redirect("admin_profile")
        except:
            messages.error(request, f"Ошибка сохранения данных.")

    return render(request, "users/profile.html", context=user_data)
