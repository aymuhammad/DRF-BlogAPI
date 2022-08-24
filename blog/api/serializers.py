from csv import field_size_limit
from dataclasses import fields
from statistics import mode
import turtle
from rest_framework import serializers
# users are created from the User model defined in django.contrib.auth
from django.contrib.auth.models import User
from . models import Post

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source = 'owner.username')

    class Meta:
        model = Post
        fields = ['id', 'title', 'body', 'owner']

class UserSerializer(serializers.ModelSerializer):
    posts = serializers.PrimaryKeyRelatedField(many=True, read_only = True)

    class Meta:
        model = User
        fields = ['id', 'username', 'posts']