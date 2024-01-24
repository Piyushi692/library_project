from django.db import IntegrityError
from django.shortcuts import get_object_or_404
from django.test import TransactionTestCase
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Author, Book, Genre
from .serializers import AuthorSerializer, BookSerializer, GenreSerializer
from .utils import generate_author_id
import csv
from django.http import HttpResponse

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    def list(self, request, *args, **kwargs):
        authors = self.get_queryset()
        serializer = self.get_serializer(authors, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def export_books(self, request, *args, **kwargs):
        author_id = self.kwargs.get('pk')
        author = self.get_object()
        genre_id = request.data.get('genre_id')  # Assuming you send genre_id in the request data
        books = Book.objects.filter(author=author, genre__id=genre_id)

        # Create a CSV response
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="books_export.csv"'

        writer = csv.writer(response)
        writer.writerow(['Book Name', 'Genre', 'Number of Pages', 'Cover Image'])  # Add other relevant fields

        for book in books:
            writer.writerow([book.name, book.genre.name, book.pages, book.cover_image.url])

        return response
    
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def list(self, request, *args, **kwargs):
        author_id = self.kwargs.get('author_id')
        books = Book.objects.filter(author__id=author_id)
        serializer = self.get_serializer(books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def perform_create(self, serializer):
        author_id = self.kwargs.get('author_id')
        author = get_object_or_404(Author, id=author_id)
        serializer.save(author=author)

    def perform_update(self, serializer):
        author_id = self.kwargs.get('author_id')
        author = get_object_or_404(Author, id=author_id)
        serializer.save(author=author)

class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

    def perform_destroy(self, instance):
        # Check if any books are associated with the genre before deleting
        if instance.book_set.exists():
            return Response({"error": "Cannot delete genre with associated books."}, status=status.HTTP_400_BAD_REQUEST)
        instance.delete()
