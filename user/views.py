from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib import auth
from django.urls import reverse

from user.models import User
from user.forms import UserLoginForm


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return redirect(reverse('todolist'))
    else:
        form = UserLoginForm()


    return render(request, 'user/login_form.html',
                  context={
                      'title': 'Login',

                      'form': form
                  }
                  )


def register(request):
    return render(request, 'user/registry_form.html',
                  context={
                      'title': 'Register'
                  }
                  )


@login_required
def cabinet(request):
    if request.method == 'POST':
        logout(request)
        return redirect('todolist')

    return render(request, 'user/html_user_cabinet.html',
                  context={
                      'title': 'Cabinet',
                      'username': request.user.username
                  }
                  )
