import email
import turtle
from csv import field_size_limit
from dataclasses import fields
from distutils.file_util import write_file
from importlib.metadata import requires
from statistics import mode
from wsgiref import validate
from wsgiref.validate import validator

# users are created from the User model defined in django.contrib.auth
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from pyexpat import model
# registration details
from rest_framework import serializers, status
from rest_framework.validators import UniqueValidator

from .models import Comment, Post


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source = 'owner.username')
    comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'body', 'owner', 'comments']

class UserSerializer(serializers.ModelSerializer):
    posts = serializers.PrimaryKeyRelatedField(many=True, read_only = True)
    comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'posts', 'comments']

class CommentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Comment
        fields = ['id', 'body', 'owner', 'post']

# serializer to get user details using Django Token authentication
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'username']

# serializers to register user
class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True, validators=[UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(write_only = True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'email', 'first_name', 'last_name')
        extra_kwargs = {'first_name':{'required':True}, 'last_name':{'required':True}}

    # define validations conditions
    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({'password':"password fields didn't match."})
        return attrs

    def create(self, validated_data):
        user = User.objects.create(username=validated_data['username'], email=validated_data['email'], first_name=validated_data['first_name'],
                                    last_name=validated_data['last_name'])
        user.set_password(validated_data['password'])
        user.save()
        return user
