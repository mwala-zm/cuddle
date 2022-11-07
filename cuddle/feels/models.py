from django.db import models
import uuid
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.
class User(models.Model):
    id = models.CharField(
        primary_key=True,
        max_length=40,
        null=False,
        unique=True,
        blank=False,
        default=uuid.uuid4,
    )
    user_name = models.CharField(max_length=255, blank=False, null=False)
    first_name = models.CharField(max_length=255, blank=False, null=False)
    last_name = models.CharField(max_length=40, blank=False, null=False)
    # User Gender:
    default_answer = 0
    male = 1
    female = 2
    gender_type = (
        (default_answer, "Default"),
        (male, "Male"),
        (female, "Female"),
    )
    gender = models.IntegerField(choices=gender_type, null=False, blank=False)
    email = models.EmailField(max_length=255, blank=True, null=False)
    phone_number = PhoneNumberField(blank=True)
    dob = models.DateField(blank=True, null=True)
    country = CountryField()

    def __str__(self):
        return "{}{}".format(self.first_name, self.last_name)


class Movie(models.Model):
    title = models.CharField(max_length=255, blank=False, null=False)
    genre = models.CharField(max_length=255, blank=False, null=False)
    year = models.DateField(blank=True, null=True)
    url = models.URLField()

    def __str__(self):
        return "{}".format(self.title)


class Music(models.Model):
    title = models.CharField(max_length=255, blank=True, null=False)
    artist = models.CharField(max_length=255, blank=True, null=False)
    album = models.CharField(max_length=255, blank=True, null=False)
    year = models.DateField(blank=True, null=False)
    genre = models.CharField(max_length=255, blank=True, null=False)
    url = models.URLField()

    def __str__(self):
        return "{}{}".format(self.title, self.artist)
