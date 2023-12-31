# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


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


class Contracts(models.Model):
    id_contract = models.AutoField(
        db_column="ID_contract", primary_key=True
    )  # Field name made lowercase.
    datecontractstart = models.DateField(
        db_column="DateContractStart", blank=True, null=True
    )  # Field name made lowercase.
    contractdays = models.IntegerField(
        db_column="ContractDays", blank=True, null=True
    )  # Field name made lowercase.
    paymentstatus = models.IntegerField(
        db_column="PaymentStatus", blank=True, null=True
    )  # Field name made lowercase.
    id_group = models.ForeignKey(
        "Group", models.DO_NOTHING, db_column="ID_group", blank=True, null=True
    )  # Field name made lowercase.
    id_instructor = models.ForeignKey(
        "Instructors",
        models.DO_NOTHING,
        db_column="ID_instructor",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    id_student = models.ForeignKey(
        "Students", models.DO_NOTHING, db_column="ID_student"
    )  # Field name made lowercase.
    id_plan = models.ForeignKey(
        "Planseducations", models.DO_NOTHING, db_column="ID_plan"
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "Contracts"


class Drivingcategories(models.Model):
    id_category = models.AutoField(
        db_column="ID_category", primary_key=True
    )  # Field name made lowercase.
    name = models.TextField(db_column="Name")  # Field name made lowercase.
    price = models.IntegerField(
        db_column="Price", blank=True, null=True
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "DrivingCategories"


class Group(models.Model):
    id_group = models.AutoField(
        db_column="ID_group", primary_key=True
    )  # Field name made lowercase.
    id_lecture = models.ForeignKey(
        "Lectures", models.DO_NOTHING, db_column="ID_lecture"
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "Group"


class Instructors(models.Model):
    id_instructor = models.OneToOneField(
        "Users", models.DO_NOTHING, db_column="ID_instructor", primary_key=True
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


class Lectures(models.Model):
    id_lecture = models.OneToOneField(
        "Users", models.DO_NOTHING, db_column="ID_lecture", primary_key=True
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "Lectures"


class Planseducations(models.Model):
    id_plan = models.AutoField(
        db_column="ID_plan", primary_key=True
    )  # Field name made lowercase.
    name = models.TextField(db_column="Name")  # Field name made lowercase.
    theoretical_time = models.IntegerField(
        db_column="Theoretical_time", blank=True, null=True
    )  # Field name made lowercase.
    practise_time = models.IntegerField(
        db_column="Practise_time", blank=True, null=True
    )  # Field name made lowercase.
    id_category = models.ForeignKey(
        Drivingcategories, models.DO_NOTHING, db_column="ID_category"
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "PlansEducations"


class Students(models.Model):
    id_student = models.OneToOneField(
        "Users", models.DO_NOTHING, db_column="ID_student", primary_key=True
    )  # Field name made lowercase.
    passexam = models.IntegerField(
        db_column="PassExam", blank=True, null=True
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "Students"


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

    class Meta:
        managed = True
        db_table = "Users"


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = "auth_group"


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey("AuthPermission", models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = "auth_group_permissions"
        unique_together = (("group", "permission"),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey("DjangoContentType", models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = "auth_permission"
        unique_together = (("content_type", "codename"),)


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


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = "auth_user_groups"
        unique_together = (("user", "group"),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = "auth_user_user_permissions"
        unique_together = (("user", "permission"),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey(
        "DjangoContentType", models.DO_NOTHING, blank=True, null=True
    )
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = "django_admin_log"


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = "django_content_type"
        unique_together = (("app_label", "model"),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = "django_migrations"


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = "django_session"


class SchoolProfile(models.Model):
    id = models.BigAutoField(primary_key=True)
    image = models.CharField(max_length=100)
    user = models.OneToOneField(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = "school_profile"
