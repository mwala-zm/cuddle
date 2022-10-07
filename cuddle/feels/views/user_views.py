from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# from rest_framework import permissions
from feels.models import User
from feels.serializers import UserSerializer


class UsersView(APIView):
    def get(self, request, *args, **kwargs):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        data = {
            "user_name": request.data.get("user_name"),
            "first_name": request.data.get("first_name"),
            "last_name": request.data.get("last_name"),
            "email": request.data.get("email"),
            "gender": request.data.get("gender"),
            "phone": request.data.get("phone"),
            "dob": request.data.get("dob"),
        }
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetails(APIView):
    def get_object(self, user_id):
        try:
            return User.objects.get(id=user_id)
        except User.DoesNotExist:
            return None

    def get(self, request, user_id, *args, **kwargs):
        user_instance = self.get_object(user_id)
        if not user_instance:
            return Response(
                {"res": "This user does not exist"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        serializer = UserSerializer(user_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, user_id, *args, **kwargs):
        user_instance = self.get_object(user_id)
        if not user_instance:
            return Response(
                {"res": "User does not exists"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        data = {
            "user_name": request.data.get("user_name"),
            "first_name": request.data.get("first_name"),
            "last_name": request.data.get("last_name"),
            "gender": request.data.get("gender"),
            "email": request.data.get("email"),
            "phone": request.data.get("phone"),
            "dob": request.data.get("dob"),
        }

        serializer = UserSerializer(instance=user_instance, data=data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, user_id, *args, **kwargs):
        user_instance = self.get_object(user_id)
        if not user_instance:
            return Response(
                {"res": "This user does not exist"}, status=status.HTTP_400_BAD_REQUEST
            )
        user_instance.delete()
        return Response(
            {"res": "The user has been deleted!"},
            status=status.HTTP_200_OK,
        )
