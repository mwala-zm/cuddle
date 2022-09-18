# Generated by Django 4.0.6 on 2022-09-18 09:39

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.CharField(default=uuid.uuid4, max_length=40, primary_key=True, serialize=False, unique=True)),
                ('username', models.CharField(max_length=40, null=True)),
                ('email', models.EmailField(blank=True, max_length=255, null=True)),
                ('phone', models.CharField(blank=True, max_length=255, null=True)),
                ('dob', models.DateField(blank=True, null=True)),
            ],
        ),
    ]
