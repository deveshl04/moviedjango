from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import Movies
from . serializer import MoviesSerializer


class MovieList(APIView):

    def get(self, request):
        movie1 = Movies.objects.all()
        serializer = MoviesSerializer(movie1, many=True)
        return Response(serializer.data)

    def post(self, request):
        movie_data = request.data
        newMovie = Movies.objects.create(id=movie_data['id'], movie_name = movie_data['movie_name'],director = movie_data['director'], genre = movie_data['genre'], rating = movie_data['rating'],release_date = movie_data['release_date'])
        newMovie.save()
        serializer = MoviesSerializer(newMovie)
        return Response(serializer.data)