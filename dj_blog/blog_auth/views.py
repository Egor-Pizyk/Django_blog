from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from blog_auth.forms import UserCreate, UserAuthForm


class UserRegister(CreateView):
    model = User
    form_class = UserCreate
    template_name = 'blog_auth/user_register.html'
    success_url = reverse_lazy('blog_auth:login')


class AuthUserView(LoginView):
    authentication_form = UserAuthForm
    template_name = 'blog_auth/user_auth.html'

    def get_success_url(self):
        return reverse_lazy('blog:main-page')


@login_required()
def user_logout(request):
    logout(request)
    return redirect('blog:main-page')
