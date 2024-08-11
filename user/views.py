from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib import auth
from django.urls import reverse

from user.models import User
from user.forms import UserLoginForm, UserRegistrationForm, UserCabinetForm


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
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('login'))
    else:
        form = UserRegistrationForm()

    return render(request, 'user/registry_form.html',
                  context={
                      'title': 'Register',

                      'form': form
                  }
                  )


@login_required
def cabinet(request):
    if request.method == 'POST':
        form = UserCabinetForm(instance=request.user, data=request.POST, files=request.FILES)
        if 'quit' in request.POST:
            logout(request)
            return redirect('todolist')

        elif 'save-cabinet' in request.POST:
            if form.is_valid():
                form.save()
                return redirect(reverse('cabinet'))

    else:
        form = UserCabinetForm(instance=request.user)

    return render(request, 'user/html_user_cabinet.html',
                  context={
                      'title': 'Cabinet',

                      'form': form
                  }
                  )
