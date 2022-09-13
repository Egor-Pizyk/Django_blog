from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.db.models import Avg, ExpressionWrapper, Value, Sum
from django.forms import FloatField
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView

from blog.forms import UserCreate, UserAuthForm
from blog.models import Post, Rating


class UserRegister(CreateView):
    model = User
    form_class = UserCreate
    template_name = 'blog/user_register.html'
    success_url = reverse_lazy('blog:login')


class AuthUserView(LoginView):
    authentication_form = UserAuthForm
    template_name = 'blog/user_auth.html'

    def get_success_url(self):
        return reverse_lazy('blog:main-page')


@login_required()
def user_logout(request):
    logout(request)
    return redirect('blog:main-page')


class PostsList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('blog:login')
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context.update(rating=Rating.objects.all())
    #     return context


class PostDetail(LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'


@login_required()
def index(request):
    return HttpResponse('ok')


