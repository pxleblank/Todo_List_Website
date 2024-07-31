from django.shortcuts import render
from django.http import HttpResponse


def todolist(request):
    return render(request, 'todo/htmltodolist.html',

                  )

def cabinet(request):
    return render(request, 'todo/cabinet.html',

                  )
