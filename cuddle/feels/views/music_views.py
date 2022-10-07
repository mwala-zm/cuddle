from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# from rest_framework import permissions
from feels.models import Music
from feels.serializers import MusicSerializer


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
