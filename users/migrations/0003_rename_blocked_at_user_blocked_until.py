# Generated by Django 4.1.7 on 2023-03-09 18:50

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0002_user_blocked_at"),
    ]

    operations = [
        migrations.RenameField(
            model_name="user",
            old_name="blocked_at",
            new_name="blocked_until",
        ),
    ]
