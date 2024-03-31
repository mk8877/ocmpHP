# Generated by Django 4.2.2 on 2024-03-31 03:07

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("toppage", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Member",
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
                ("name_roman", models.CharField(max_length=100)),
                ("research", models.CharField(max_length=100)),
                ("comment", models.TextField()),
                ("hometown", models.CharField(max_length=100)),
                ("is_AssistantProfessor", models.BooleanField(default=False)),
                ("is_Researcher", models.BooleanField(default=False)),
                ("is_PhD", models.BooleanField(default=False)),
                ("is_Master2", models.BooleanField(default=False)),
                ("is_Master1", models.BooleanField(default=False)),
                ("is_Bachelor", models.BooleanField(default=False)),
                ("is_public", models.BooleanField(default=True)),
            ],
        ),
    ]