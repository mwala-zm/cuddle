from django.urls import path, include

# Importing all views from feels.views Directory
from feels.views.user_views import UsersView

from feels.views.music_views import exchange_token

from feels.views.movie_views import get_trending, get_movie_by_genre

urlpatterns = [
    path("users/", UsersView.as_view()),
    path("exchange_token/", exchange_token),
    path("trending/", get_trending, name="get_trending"),
    path("movies/<int:genre_id>/", get_movie_by_genre, name="get_movie_by_genre"),
]
