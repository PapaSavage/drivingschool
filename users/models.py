from django.db import models


class Users(models.Model):
    id_user = models.OneToOneField(
        "AuthUser", models.DO_NOTHING, db_column="ID_user", primary_key=True
    )  # Field name made lowercase.
    surname = models.TextField(
        db_column="Surname", blank=True, null=True
    )  # Field name made lowercase.
    name = models.TextField(
        db_column="Name", blank=True, null=True
    )  # Field name made lowercase.
    secondname = models.TextField(
        db_column="SecondName", blank=True, null=True
    )  # Field name made lowercase.
    adress = models.TextField(
        db_column="Adress", blank=True, null=True
    )  # Field name made lowercase.
    telephone = models.TextField(
        db_column="Telephone", blank=True, null=True
    )  # Field name made lowercase.
    dateofbirth = models.CharField(
        db_column="DateOfBirth", max_length=10, blank=True, null=True
    )  # Field name made lowercase.
    passport = models.TextField(
        db_column="Passport", blank=True, null=True
    )  # Field name made lowercase.
    seriamedicalcertificate = models.TextField(
        db_column="SeriaMedicalCertificate", blank=True, null=True
    )  # Field name made lowercase.
    is_admin = models.IntegerField()
    email = models.CharField(max_length=50)

    # def __str__(self):
    #     return str(self.surname + self.name + self.secondname)

    class Meta:
        managed = True
        db_table = "Users"


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = "auth_user"


# Create your models here.
