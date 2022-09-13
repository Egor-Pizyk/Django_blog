from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Post(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    content = models.TextField()
    create_dt = models.DateTimeField(auto_now_add=True)
    update_dt = models.DateTimeField(auto_now=True)
    rating = models.ManyToManyField('Rating', null=True, blank=True)
    comments = models.ManyToManyField('Comments', null=True, blank=True)

    @property
    def test(self):
        print('qwe')
        return 'qwe'

    def get_absolute_url(self):
        return reverse('blog:post-detail', kwargs={'slug': self.slug})


class Comments(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    create_dt = models.DateTimeField(auto_now_add=True)


class Rating(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    value = models.IntegerField()

    def __str__(self):
        return str(self.value)
