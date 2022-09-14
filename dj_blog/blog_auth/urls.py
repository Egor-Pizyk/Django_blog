from django.urls import path

from .views import *


app_name = 'blog_auth'
urlpatterns = [
    path("register/", UserRegister.as_view(), name='register'),
    path("login/", AuthUserView.as_view(), name='login'),
    path("logout/", user_logout, name='logout'),

]