from django.db import models
from django.core.validators import MaxLengthValidator
from users.models import User


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=150)
    pages = models.IntegerField(
        validators=[
        MaxLengthValidator(5)
        ]
    )
    publishing_company = models.CharField(max_length=50)
    user = models.ManyToManyField(
        User,
        through="followings.Following",
        related_name="books"
    )