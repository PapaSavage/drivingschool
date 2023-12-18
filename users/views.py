from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.db import connection
from django.contrib.auth.decorators import login_required
from .models import Users


# Create your views here.
@login_required
def home(request):
    return render(request, "users/home.html")


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


@login_required
def profile(request):
    user_data = Users.objects.get(id_user=request.user.id)
    context = {"user_data": user_data}

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
    else:
        user_data = Users.objects.get(id_user=request.user.id)
        context = {"user_data": user_data}

    return render(request, "users/profile.html", context=context)
