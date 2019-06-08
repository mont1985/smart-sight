from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

ROLES = (
    ('ADMIN', 'Admin'),
    ('DOCTOR', 'Doctor'),
    ('SUPERUSER', 'SuperUSer')
)

LEVELS = (
    ('TIER 1', 'Level 1'),
    ('TIER 2', 'Level 2'),
    ('TIER 3', 'Level 3'),
    ('TIER 4', 'Level 4')
)

GENDER = (
    ('M', 'Male'),
    ('F', 'Female')
)

STATUS = (
    ('SINGLE', 'Single'),
    ('MARRIED', 'Married'),
    ('DIVORCED', 'Divorced'),
    ('SEPARATED', 'Separated')
)

DIAGNOSIS = (
    ('DME', 'Diabetic macular edema'),
    ('AMD', 'Age-related macular degeneration'),
    ('NORMAL', 'Normal')
)


class User(AbstractUser):
    username = models.CharField(blank=True, null=True, max_length=255)
    email = models.EmailField(_('email address'), unique=True)
    title = models.CharField(choices=ROLES, max_length=9)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name', 'title']

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)


class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name='profile')
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    address = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=5)
    photo = models.ImageField(upload_to='profile_photos', blank=True)
    bio = models.CharField(max_length=255)

    def __str__(self):
        return "{}'s profile".format(self.user)


class Hospital(models.Model):
    name = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=5)
    level = models.CharField(choices=LEVELS, max_length=6)
    administrator = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='administrator',
        limit_choices_to={'title': 'ADMIN'})
    doctors = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='practitioners',
        limit_choices_to={'title': 'DOCTOR'})

    def __str__(self):
        return self.name


class Patient(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(null=False)
    gender = models.CharField(choices=GENDER, max_length=1)
    identification = models.CharField(max_length=20)
    email = models.EmailField()
    contact = models.CharField(max_length=15)
    marital_status = models.CharField(choices=STATUS, max_length=10)
    county = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=5)

    def __str__(self):
        return self.name


class PatientDiagnoses(models.Model):
    patient = models.ForeignKey(
        Patient,
        on_delete=models.PROTECT,
        related_name='appointments')
    image = models.ImageField(upload_to='eye_photos/')
    model_diagnosis = models.CharField(choices=DIAGNOSIS, max_length=7, null=True)
    is_true = models.BooleanField(default=False)
    doctors_comment = models.CharField(max_length=255, null=True)
    doctor = models.ForeignKey(
        User,
        related_name='physician',
        on_delete=models.PROTECT,
        limit_choices_to={'title': 'DOCTOR'})
    hospital_visited = models.ForeignKey(
        Hospital,
        on_delete=models.PROTECT,
        related_name='hospital_visited', )

    def __str__(self):
        return "{}'s profile".format(self.patient)
