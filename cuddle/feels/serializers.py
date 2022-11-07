from rest_framework import serializers
from .models import User, Music, Movie


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["user_name", "first_name", "gender", "email", "phone_number", "dob", "country"]


class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music
        fields = ["title", "genre", "artist", "album", "year", "url"]


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ["title", "genre", "year", "url"]
