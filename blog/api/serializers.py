from dataclasses import fields
from statistics import mode
from rest_framework import serializers
# users are created from the User model defined in django.contrib.auth
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']