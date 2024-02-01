import os
import requests

from datetime import datetime
from django.shortcuts import render
from django.http import JsonResponse
from dotenv import load_dotenv

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# from rest_framework import permissions
from feels.models import Movie
from feels.serializers import MovieSerializer


load_dotenv()


def get_trending(request):
    tmdb_api_key = os.environ.get("TMDB_API")
    tmdb_url = f"https://api.themoviedb.org/3/trending/movie/week?api_key={tmdb_api_key}&language=en-US"

    response = requests.get(tmdb_url)
    if response.status_code == 200:
        movie_data = response.json().get("results", [])[:25]
        # Process and extract information from movie_data as needed
        return JsonResponse({"movies" :movie_data})
    else:
        return JsonResponse({"error": "Failed to fetch movie details"}, status=500)


def get_movie_by_genre(request, genre_id):
    tmdb_api_key = os.environ.get("TMDB_API")
    current_year = datetime.now().year
    release_date_cutoff = f"{current_year - 22}-01-01"
    tmdb_url = f"https://api.themoviedb.org/3/trending/movie?api_key={tmdb_api_key}&with_genres={genre_id}&language=en-US"

    response = requests.get(tmdb_url)

    if response.status_code == 200:
        movie_data = response.json().get("results", [])[:100]
        # Process and extract information from movie_data as needed
        return JsonResponse({"movies": movie_data})
    else:
        return JsonResponse({"error": "Failed to fetch movie details"}, status=500)


class MovieList(APIView):
    def get(self, request, *args, **kwargs):
        users = Movie.objects.all()
        serializer = MovieSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        data = {
            "title": request.data.get("title"),
            "genre": request.data.get("genre"),
            "year": request.data.get("year"),
            "url": request.data.get("url"),
        }
        serializer = MovieSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
