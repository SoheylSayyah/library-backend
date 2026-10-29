from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = [
            "id",
            "title",
            "created_at",
            "updated_at",
            "is_active",
            "is_deleted",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]
