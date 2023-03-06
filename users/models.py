from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.fields import ArrayField


class User(AbstractUser):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=150, unique=True)
    is_employee = models.BooleanField(default=False, null=True, blank=True)
    is_blocked = models.BooleanField(default=False, null=True, blank=True)
    current_books = ArrayField(models.CharField(max_length=200), null=True, blank=True, default=None)