from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

ROLES = (
    ('ADM', 'Admin'),
    ('DOC', 'Doctor')
)


class User(AbstractUser):
    username = models.CharField(blank=True, null=True, max_length=255)
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    def __str__(self):
        return "{}".format(self.email)


class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    title = models.CharField(choices=ROLES, max_length=5)
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    address = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=5)
    photo = models.ImageField(upload_to='profile_photos', blank=True)
    bio = models.CharField(max_length=255)

    def __str__(self):
        return "{}'s profile".format(self.user)
