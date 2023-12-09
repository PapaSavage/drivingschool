from django.shortcuts import render
from django.db import connection


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
