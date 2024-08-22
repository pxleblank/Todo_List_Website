"""
URL configuration for tasks project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from todo.views import todolist, delete_task, change_state, AddTaskInTodoListForm
# from todo.forms import AddTaskInTodoListForm
from user.views import cabinet, login, register

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include('todo.urls'))
    path('', todolist, name='todolist'),
    path('cabinet/', cabinet, name='cabinet'),
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('task/delete/<int:task_id>/', delete_task, name='delete_task'),
    path('task/change_state/<int:task_id>/', change_state, name='change_state'),
    path('task/add/', AddTaskInTodoListForm.as_view(), name='add_task')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
