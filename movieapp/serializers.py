from django.contrib.auth.models import User
from rest_framework import serializers
from movieapp.models import Movie, Person


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):

    actors = serializers.SlugRelatedField(many=True, slug_field='name', queryset=Person.objects.all())
    director = serializers.SlugRelatedField(slug_field='name', queryset=Person.objects.all())

    class Meta:
        model = Movie
        fields = '__all__'


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')
