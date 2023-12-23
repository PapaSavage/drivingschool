from django.db import connection


def admin_exist(request):
    with connection.cursor() as cursor:
        cursor.execute(
            "Select is_admin from Users where ID_user = %s", (request.user.id,)
        )
        row = cursor.fetchone()
    if row:
        return True
    else:
        return False


def student_exist(request):
    with connection.cursor() as cursor:
        cursor.execute(
            "Select ID_student from Students where ID_student = %s", (request.user.id,)
        )
        row = cursor.fetchone()
    if row:
        return True
    else:
        return False


def instructor_exist(request):
    with connection.cursor() as cursor:
        cursor.execute(
            "Select ID_instructor from Instructors where ID_instructor = %s",
            (request.user.id,),
        )
        row = cursor.fetchone()
    if row:
        return True
    else:
        return False


def lecture_exist(request):
    with connection.cursor() as cursor:
        cursor.execute(
            "Select ID_lecture from Lectures where ID_lecture = %s", (request.user.id,)
        )
        row = cursor.fetchone()
    if row:
        return True
    else:
        return False
