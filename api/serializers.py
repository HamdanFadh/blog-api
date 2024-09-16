from rest_framework import serializers
from django.contrib.auth.models import User
from api.models import Post, Category

class UserSerializers(serializers.ModelSerializer):
    posts = serializers.PrimaryKeyRelatedField(many = True, read_only = True)
    categories = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'posts', 'categories']

class PostSerializers(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    class Meta:
        model = Post
        fields = ['id', 'title', 'created_at',  'categories', 'author', 'body']

class CategorySerializers(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    posts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'author', 'posts']