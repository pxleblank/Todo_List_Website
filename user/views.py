from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# from user.models import User


def login(request):
    return render(request, 'user/login_form.html',
                  context={
                        'title': 'Login'
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
