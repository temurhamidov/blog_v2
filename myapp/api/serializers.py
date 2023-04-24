from rest_framework import serializers
from myapp.models import Blog, Category, Comment

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'id',
            'name',
            'image',
            'text',
        ]


class BlogSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    class Meta:
        model = Blog
        fields = [
            'id',
            'title',
            'image',
            'text',
            'category',
        ]


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = [
            'id',
            'text',
            'comment',
            'blog',
            'rating',
        ]