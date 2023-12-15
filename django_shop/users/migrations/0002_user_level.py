# Generated by Django 3.2.23 on 2023-12-14 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="level",
            field=models.CharField(
                choices=[("admin", "admin"), ("user", "user")],
                default="user",
                max_length=8,
                verbose_name="등급",
            ),
            preserve_default=False,
        ),
    ]
