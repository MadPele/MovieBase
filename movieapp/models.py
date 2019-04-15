from django.db import models


class Person(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name='Name'
    )

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Person'
        verbose_name_plural = 'Persons'


class Movie(models.Model):
    title = models.CharField(
        max_length=55,
        verbose_name='Title'
    )
    director = models.ForeignKey(
        Person,
        related_name='movie_director',
        null=True,
        on_delete=models.SET_NULL
    )
    actors = models.ManyToManyField(
        Person,
        related_name='movie_actor',
    )
    release_year = models.PositiveSmallIntegerField(verbose_name='Release year')
    description = models.TextField(verbose_name='Description')

    def __str__(self):
        return f'{self.title} ({self.release_year})'

    class Meta:
        verbose_name = 'Movie'
        verbose_name_plural = 'Movies'
