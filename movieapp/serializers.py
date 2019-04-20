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
        return (date.today() - obj.date_of_birthday).days


class ActorSerializer(serializers.ModelSerializer):

    actor = serializers.SlugRelatedField(slug_field='name', queryset=Person.objects.exclude(actor__in=Actor.objects.all()))

    class Meta:
        model = Actor
        fields = ('id', 'actor', 'url')


class DirectorSerializer(serializers.ModelSerializer):

    director = serializers.SlugRelatedField(slug_field='name', queryset=Person.objects.exclude(director__in=Director.objects.all()))

    class Meta:
        model = Director
        fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):

    actors = serializers.HyperlinkedRelatedField(many=True, queryset=Actor.objects.all(), view_name='actor-detail')
    director = serializers.PrimaryKeyRelatedField(queryset=Director.objects.all())

    class Meta:
        model = Movie
        fields = '__all__'


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')
