# Generated by Django 4.0.6 on 2022-11-07 16:02

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('feels', '0017_alter_user_gender'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='phone',
        ),
        migrations.AddField(
            model_name='user',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None),
        ),
    ]