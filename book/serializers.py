from rest_framework import serializers
from .models import Book


class GetAllBooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id','name', 'author', 'topic', 'description', 'imageUrl')
