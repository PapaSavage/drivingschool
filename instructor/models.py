from django.db import models
from users.models import Users


# Create your models here.
class Cars(models.Model):
    id_car = models.AutoField(
        db_column="ID_car", primary_key=True
    )  # Field name made lowercase.
    model = models.TextField(db_column="Model")  # Field name made lowercase.
    color_auto = models.TextField(
        db_column="Color_auto", blank=True, null=True
    )  # Field name made lowercase.
    rented = models.TextField(
        db_column="Rented", blank=True, null=True
    )  # Field name made lowercase.
    reg_number_auto = models.IntegerField(
        db_column="Reg_number_auto"
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "Cars"


class Instructors(models.Model):
    id_instructor = models.OneToOneField(
        Users, models.DO_NOTHING, db_column="ID_instructor", primary_key=True
    )  # Field name made lowercase.
    id_car = models.ForeignKey(
        Cars, models.DO_NOTHING, db_column="ID_car", blank=True, null=True
    )  # Field name made lowercase.
    rating = models.IntegerField(
        db_column="Rating", blank=True, null=True
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "Instructors"
