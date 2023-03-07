from django.db import models
from users.models import User


class Copy(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=150)
    pages = models.CharField(max_length=5)
    publishing_company = models.CharField(max_length=50)
    isbn = models.CharField(max_length=13)
    is_loaned = models.BooleanField(
        default=False, 
        null=True, 
        blank=True
        )
    user = models.ManyToManyField(
        User,
        through="loans.Loan",
        related_name="current_books"
    )
    book = models.ForeignKey(
        "books.Book",
        on_delete=models.CASCADE,
        related_name="copies"
        )

