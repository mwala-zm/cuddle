# Generated by Django 4.0.6 on 2022-09-18 12:27

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("feels", "0014_alter_user_gender"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="gender",
            field=models.IntegerField(
                choices=[
                    (0, "Default"),
                    (1, "Male"),
                    (2, "Female"),
                    (3, "Rather Not specify"),
                ]
            ),
        ),
    ]
