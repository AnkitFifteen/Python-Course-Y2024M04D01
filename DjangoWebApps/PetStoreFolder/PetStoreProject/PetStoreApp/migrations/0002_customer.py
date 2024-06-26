# Generated by Django 5.0.6 on 2024-05-31 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("PetStoreApp", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Customer",
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
                ("name", models.CharField(max_length=200)),
                ("email", models.EmailField(max_length=254)),
                ("phone", models.BigIntegerField()),
                ("password", models.CharField(max_length=200)),
            ],
            options={
                "db_table": "Customer",
            },
        ),
    ]
