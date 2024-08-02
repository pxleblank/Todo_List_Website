from django.shortcuts import render


def cabinet(request):
    return render(request, 'user/html_user_cabinet.html',
                  context={
                      'title': 'Cabinet'
                  }
                  )
