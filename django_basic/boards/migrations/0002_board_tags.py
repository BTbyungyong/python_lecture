# Generated by Django 3.2.23 on 2023-12-14 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tags", "0001_initial"),
        ("boards", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="board",
            name="tags",
            field=models.ManyToManyField(to="tags.Tag", verbose_name="태그"),
        ),
    ]