from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# from user.models import User


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
