# Generated by Django 4.0.6 on 2022-09-18 11:48

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("feels", "0009_alter_movie_genre_alter_movie_title_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="first_name",
            field=models.CharField(blank=True, max_length=40),
        ),
        migrations.AlterField(
            model_name="user",
            name="last_name",
            field=models.CharField(blank=True, max_length=40),
        ),
        migrations.AlterField(
            model_name="user",
            name="user_name",
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
