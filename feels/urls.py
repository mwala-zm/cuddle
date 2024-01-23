from django.urls import path, include

# Importing all views from feels.views Directory
from feels.views.user_views import UsersView, UserDetails

from feels.views.music_views import MusicListView

from feels.views.movie_views import MovieList

urlpatterns = [
    path("users/", UsersView.as_view()),
    path("users/<uuid:user_id>/change", UserDetails.as_view()),
    path("music/", MusicListView.as_view()),
    path("movies/", MovieList.as_view()),
]
