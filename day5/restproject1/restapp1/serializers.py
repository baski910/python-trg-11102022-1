from dataclasses import fields
from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    booktitle = serializers.CharField(max_length=50)
    bookauthor = serializers.CharField(max_length=50)
    class Meta:
        model = Book
        fields = ('__all__')