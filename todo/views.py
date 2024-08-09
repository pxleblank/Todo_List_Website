from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from todo.models import Todolist


@login_required
def todolist(request):
    if request.method == 'POST':
        if 'post_contents' in request.POST:
            task_content = request.POST.get('post_contents')
            if task_content:
                Todolist.objects.create(user=request.user, task=task_content)
                return redirect(reverse('todolist'))
        elif 'delete_task' in request.POST:
            task_id = request.POST.get('delete_task')
            Todolist.objects.filter(user=request.user, id=task_id).delete()
            return redirect(reverse('todolist'))
        elif 'change_state' in request.POST:
            task_id = request.POST.get('change_state')
            task = Todolist.objects.get(user=request.user, id=task_id)
            task.state = 'completed' if task.state == 'in progress' else 'in progress'
            task.save()
            return redirect(reverse('todolist'))


    return render(request, 'todo/html_todo_list.html',
                  context={
                      'title': 'Todo List',
                      'user': request.user.username,
                      'is_tasks': Todolist.objects.filter(user=request.user).exists(),
                      'tasklist': Todolist.objects.filter(user=request.user),
                  }
                  )
