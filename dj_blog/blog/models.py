from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)
    content = models.TextField()
    create_dt = models.DateTimeField(auto_now_add=True)
    update_dt = models.DateTimeField(auto_now=True)
    rating = models.ForeignKey('Rating', on_delete=models.CASCADE)
    comments = models.ManyToManyField('Comments')


class Comments(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    create_dt = models.DateTimeField(auto_now_add=True)


class Rating(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    value = models.IntegerField()
