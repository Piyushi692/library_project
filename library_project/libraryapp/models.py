from django.db import models
from django.contrib.auth.models import User

class Genre(models.Model):
    name = models.CharField(max_length=100)

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    city = models.CharField(max_length=100)
    profile_image = models.ImageField(upload_to='authors/')
    author_id = models.CharField(max_length=15, unique=True)

class Book(models.Model):
    title = models.CharField(max_length=200)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    pages = models.IntegerField()
    cover_image = models.ImageField(upload_to='books/')
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
