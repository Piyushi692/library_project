from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AuthorViewSet, BookViewSet, GenreViewSet

router = DefaultRouter()
router.register(r'authors', AuthorViewSet)
router.register(r'books', BookViewSet)
router.register(r'genres', GenreViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('authors/<int:pk>/export-books/', AuthorViewSet.as_view({'get': 'export_books'}), name='author-export-books'),
    # Add more custom paths as needed for your views
]
