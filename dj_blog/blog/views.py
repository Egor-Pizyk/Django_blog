from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView

from blog.models import Post


class PostsList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('blog_auth:login')
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'


class PostDetail(LoginRequiredMixin, DetailView):
    login_url = reverse_lazy('blog_auth:login')
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'




