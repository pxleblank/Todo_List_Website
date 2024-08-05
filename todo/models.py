from django.db import models
from django.contrib.auth.models import User


class Todolist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.TextField(null=False, blank=False)
    state = models.CharField(max_length=64, blank=False, null=False, default='in progress')

    def __str__(self):
        return self.task
