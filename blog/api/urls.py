from atexit import register
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

# registrations link
from .views import UserDetailAPI, RegisterUserAPIView

urlpatterns = [
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetails.as_view()),
    path('posts/', views.PostList.as_view()),
    path('posts/<int:pk>/', views.PostDetail.as_view()),
    path('comments/', views.CommentList.as_view()),
    path('comments/<int:pk>/', views.CommentDetail.as_view()),
    path('get-details/', UserDetailAPI.as_view()),
    path('register/', RegisterUserAPIView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)