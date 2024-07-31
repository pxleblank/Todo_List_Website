from django.urls import path
from . import views

urlpatterns = [
    path('', views.todolist, name='todolist'),
    path('cabinet/', views.cabinet, name='cabinet')
]