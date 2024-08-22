from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django import forms
from todo.models import Todolist


# class AddTaskInTodoListForm(CreateView):
#     task = forms.CharField(widget=forms.TextInput(attrs={'class': 'u-clearfix', 'placeholder': 'Имя пользователя'}))
#
#     class Meta:
#         model = Todolist
#         fields = ('task',)
#         success_url = reverse_lazy('todolist')
