from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import CreateView

from blog.forms import UserCreate, UserAuthForm


class UserRegister(CreateView):
    model = User
    form_class = UserCreate
    template_name = 'blog/user_register.html'
    success_url = 'login'


def user_auth(request):
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        login(request, user)
        return redirect('blog:main-page')
    else:
        form = UserAuthForm()
        return render(request, 'blog/user_auth.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('blog:main-page')


@login_required()
def index(request):
    print(request.user)
    return HttpResponse('ok')


