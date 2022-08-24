from statistics import mode
from turtle import title
from venv import create
from django.db import models

# model that inherits from Django’s Model class and define its fields
class Post(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default="")
    body = models.TextField(blank=True, default="")
    owner = models.ForeignKey('auth.User', related_name='posts', on_delete=models.CASCADE)

    class Meta:
        ordering = ['created']

# comment class
class Comment(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    body = models.TextField(blank=False)
    owner = models.ForeignKey('auth.User', related_name='comments', on_delete=models.CASCADE)
    post = models.ForeignKey('Post', related_name='comments', on_delete=models.CASCADE)

    class Meta:
        ordering = ['created']