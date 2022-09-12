from django.contrib import admin
from django.urls import path

from .views import *


app_name = 'blog'
urlpatterns = [
    path("register/", UserRegister.as_view(), name='register'),
    path("login/", user_auth, name='login'),
    path("logout/", user_logout, name='logout'),
    path("", index, name='main-page'),
]