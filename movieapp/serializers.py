from django.contrib.auth.models import User
from rest_framework import serializers
from movieapp.models import Movie, Person, Actor, Director
from datetime import date


class PersonSerializer(serializers.ModelSerializer):

    days_since_borned = serializers.SerializerMethodField()

    class Meta:
        model = Person
        fields = '__all__'

    def get_days_since_borned(self, obj):
        return (date.today()- obj.date_of_birthday).days


class ActorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Actor
        fields = '__all__'


class DirectorSerializer(serializers.ModelSerializer):

    # actor = serializers.HyperlinkedRelatedField()

    class Meta:
        model = Director
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
