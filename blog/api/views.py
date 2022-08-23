import imp
from rest_framework import generics
from api import serializers
from django.contrib.auth.models import User

# provides read-only access (via get) to the list of users
class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer

# provides read-only access (via get) to a single user
class UserDetails(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer