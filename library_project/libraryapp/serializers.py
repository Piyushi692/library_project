from rest_framework import serializers
from .models import Author, Book, Genre, User
from .utils import generate_author_id

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']

class AuthorSerializer(serializers.ModelSerializer):
    user = UserSerializer()  # Nested UserSerializer to include user details

    class Meta:
        model = Author
        fields = ['user', 'phone', 'email', 'city', 'profile_image', 'author_id']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create_user(**user_data)
        author_id = generate_author_id(validated_data['city'])

        # Exclude 'author_id' from validated_data when creating the Author instance
        validated_data.pop('author_id', None)

        author = Author.objects.create(user=user, author_id=author_id, **validated_data)
        return author

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'
