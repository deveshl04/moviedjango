from django.db import models

# Create your models here.


class Movies(models.Model):
    id = models.IntegerField(primary_key=True)
    movie_name = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    rating = models.IntegerField()
    release_date = models.DateField()

    def __str__(self):
        return self.movie_name
