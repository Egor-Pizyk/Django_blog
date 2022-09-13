from django.urls import path

from .views import *


app_name = 'blog'
urlpatterns = [
    path("register/", UserRegister.as_view(), name='register'),
    path("login/", AuthUserView.as_view(), name='login'),
    path("logout/", user_logout, name='logout'),

    path("", PostsList.as_view(), name='main-page'),
    path("detail/<slug:slug>", PostDetail.as_view(), name='post-detail')
]