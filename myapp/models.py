from django.db import models

class Game_catalagoue(models.Model):
    name = models.CharField(max_length=100)
    developer = models.CharField(max_length=100)
    release_date = models.DateField()
    rating = models.FloatField()
    genres = models.ManyToManyField('genre')
    def __str__(self):
        return self.name

class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name