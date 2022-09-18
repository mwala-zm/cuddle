from django.urls import path, include
from .views import (
    UsersView,
    UserDetails
)

urlpatterns = [
    path('users/', UsersView.as_view()),
    path('users/<uuid:user_id>/change', UserDetails.as_view()),
]