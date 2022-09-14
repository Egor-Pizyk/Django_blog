from django.urls import path

from .views import *


app_name = 'blog'
urlpatterns = [
    path("", PostsList.as_view(), name='main-page'),
    path("detail/<slug:slug>", PostDetail.as_view(), name='post-detail')
]