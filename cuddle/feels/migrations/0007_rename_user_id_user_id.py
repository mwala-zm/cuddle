# Generated by Django 4.0.6 on 2022-09-18 11:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feels', '0006_rename_id_user_user_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='user_id',
            new_name='id',
        ),
    ]