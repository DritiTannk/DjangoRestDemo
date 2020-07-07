from rest_framework import serializers
from .models import BookDetails


class BookDetailsSerializer(serializers.ModelSerializer):
    """
     ModelSerializer is useful when we can to serialize the model's data. Here, it takes model name and serialize its
     each field by it owns. To visualize it, use repr(serializer) in python console. It will representation the serialize
     field of each model field.
    """
    class Meta:
        model = BookDetails
        fields = ['id','book_name', 'author_name', 'category', 'price']
