import os
from django.shortcuts import render
from django.http import JsonResponse
import requests
import json
from dotenv import load_dotenv

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# from rest_framework import permissions
from feels.models import Music
from feels.serializers import MusicSerializer

load_dotenv()


def exchange_token(request):
    authorization_code = request.POST.get("code")

    # Make a POST request to Spotify's token endpoint
    response = requests.post(
        "https://accounts.spotify.com/api/token",
        data={
            "grant_type": "authorization_code",
            "code": authorization_code,
            "redirect_uri": os.environ.get("SPOTIFY_REDIRECT_URI"),
            "client_id": os.environ.get("SPOTIFY_CLIENT_ID"),
            "client_secret": os.environ.get("SPOTIFY_CLIENT_SECRET"),
        },
    )

    # Parse the response and send the access token back to the frontend
    data = json.loads(response.text)
    access_token = data.get("access_token")

    return JsonResponse({"access_token": access_token})


class MusicListView(APIView):
    def get(self, request, *args, **kwargs):
        users = Music.objects.all()
        serializer = MusicSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        data = {
            "title": request.data.get("title"),
            "artist": request.data.get("artist"),
            "album": request.data.get("album"),
            "genre": request.data.get("genre"),
            "year": request.data.get("year"),
            "url": request.data.get("url"),
        }
        serializer = MusicSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
