# Generated by Django 4.0.6 on 2022-09-18 10:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feels', '0003_movies_rename_username_user_user_name'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Movies',
            new_name='Movie',
        ),
    ]
