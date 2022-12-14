# Generated by Django 4.1 on 2022-08-26 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Data",
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
                ("name", models.CharField(max_length=100)),
                ("MU", models.DecimalField(decimal_places=3, max_digits=8)),
                ("csv", models.FileField(upload_to="")),
            ],
            options={"verbose_name_plural": "Data",},
        ),
    ]
