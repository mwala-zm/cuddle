# Generated by Django 4.0.6 on 2024-01-30 14:16

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("feels", "0018_remove_user_phone_user_phone_number"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
    ]
