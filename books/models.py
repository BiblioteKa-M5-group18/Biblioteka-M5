from django.db import models
from django.core.validators import MaxLengthValidator


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=150)
    pages = models.IntegerField(
        validators=[
        MaxLengthValidator(5)
        ]
    )
    publishing_company = models.CharField(max_length=50)