# Generated by Django 4.1.7 on 2023-03-08 21:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("books", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Copy",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=200)),
                ("author", models.CharField(max_length=150)),
                ("pages", models.CharField(max_length=5)),
                ("publishing_company", models.CharField(max_length=50)),
                ("isbn", models.CharField(max_length=13, unique=True)),
                (
                    "is_loaned",
                    models.BooleanField(blank=True, default=False, null=True),
                ),
                (
                    "book",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="copies",
                        to="books.book",
                    ),
                ),
            ],
        ),
    ]
