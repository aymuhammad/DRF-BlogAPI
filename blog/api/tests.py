import json
from multiprocessing.connection import Client
from unittest import TestCase
from urllib import response

from django.contrib.auth.models import User
from django.urls import reverse, resolve
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase, APIClient

from api.models import Post
from api.serializers import PostSerializer

class RegistrationTestCase(APITestCase):
    def test_registration(self):
        Client = APITestCase()
        data = {"username":"testcase", "email":"test@localhost.app", "password":"some_strong_psw", "password2":"some_strong_psw"}
        response = self.client.get("/api-auth/resgister/", data)
        # self.assertEquals(response.status_code, status.HTTP_201_CREATED)

    def  test_login(APITestCase):
        Client = APIClient()
        Client.login = {"username":"auwal123", "password":"auwal123"}
        response = APITestCase.client.post("/api-auth/login/", Client.login)
        APITestCase.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_logout(APITestCase):
        Client = APIClient()
        Client.logout()