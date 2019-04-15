from django.contrib.auth.models import User
from rest_framework import viewsets
from movieapp.models import Person, Movie
from movieapp.serializers import PersonSerializer, MovieSerializer, UserSerializer


class PersonView(viewsets.ModelViewSet):

    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class MovieView(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class UserView(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer
