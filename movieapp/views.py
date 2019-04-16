from django.contrib.auth.models import User
from rest_framework import viewsets, permissions
from movieapp.models import Person, Movie, Director, Actor
from movieapp.serializers import PersonSerializer, MovieSerializer, UserSerializer


class PersonView(viewsets.ModelViewSet):

    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class DirectorView(viewsets.ModelViewSet):

    queryset = Director.objects.all()
    serializer_class = PersonSerializer


class ActorView(viewsets.ModelViewSet):

    queryset = Actor.objects.all()
    serializer_class = PersonSerializer


class MovieView(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class UserView(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAdminUser,)
