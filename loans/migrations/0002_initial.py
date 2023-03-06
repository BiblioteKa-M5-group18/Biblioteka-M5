# Generated by Django 4.1.7 on 2023-03-06 23:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("loans", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="loan",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="loans_books",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
