from django.db import models
from django.core.validators import MaxLengthValidator, MinLengthValidator


class Copy(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=150)
    pages = models.IntegerField(
        validators=[
        MaxLengthValidator(5)
        ]
    )
    publishing_company = models.CharField(max_length=50)
    isbn = models.IntegerField(
        validators=[
        MaxLengthValidator(13),
        MinLengthValidator(13)
    ]
    )
    is_loaned = models.BooleanField(
        default=False, 
        null=True, 
        blank=True
        )
    book = models.ForeignKey(
        "books.Book",
        on_delete=models.CASCADE,
        related_name="copies"
        )

