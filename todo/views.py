from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import CreateView

from todo.models import Todolist
# from todo.forms import AddTaskInTodoListForm


class AddTaskInTodoListForm(LoginRequiredMixin, CreateView):
    model = Todolist
    fields = ['task']
    success_url = reverse_lazy('todolist')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddTaskInTodoListForm, self).form_valid(form)

@login_required
def todolist(request):
    # if request.method == 'POST':
    #     form = AddTaskInTodoListForm(data=request.POST)
    #
    #
    #
    #     if 'post_contents' in request.POST:
    #         task_content = request.POST.get('post_contents')
    #         if task_content:
    #             Todolist.objects.create(user=request.user, task=task_content)
    #             return redirect(reverse('todolist'))
    # else:
    #     form = AddTaskInTodoListForm()


    return render(request, 'todo/html_todo_list.html',
                  context={
                      'title': 'Todo List',
                      'user': request.user.username,
                      'is_tasks': Todolist.objects.filter(user=request.user).exists(),
                      'tasklist': Todolist.objects.filter(user=request.user),
                  }
                  )


def delete_task(request, task_id):
    Todolist.objects.filter(user=request.user, id=task_id).delete()
    return redirect(request.META['HTTP_REFERER'])


def change_state(request, task_id):
    task = Todolist.objects.get(id=task_id)
    task.state = 'completed' if task.state == 'in progress' else 'in progress'
    task.save()
    return redirect(request.META['HTTP_REFERER'])
