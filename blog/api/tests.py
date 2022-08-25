import json
from unittest import TestCase
from urllib import response

from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

# from api.models import Post
# from api.serializers import PostSerializer

class RegistrationTestCase(APITestCase):
    def test_registration(self):
        data = {"username":"testcase", "email":"test@localhost.app", "password":"some_strong_psw", "password2":"some_strong_psw"}
        response = self.client.get("/localhost/resgister/", data)
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)