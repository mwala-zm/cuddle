from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView
from feels.schema import schema

# Importing all views from feels.views Directory
from feels.views.user_views import UsersView, UserDetails

from feels.views.music_views import MusicListView

from feels.views.movie_views import MovieList

urlpatterns = [
    path("users/", UsersView.as_view()),
    path("users/<uuid:user_id>/change", UserDetails.as_view()),
    path("music/", MusicListView.as_view()),
    path("movies/", MovieList.as_view()),
    path("graphql", csrf_exempt(GraphQLView.as_view(graphiql=False, schema=schema))),
]
