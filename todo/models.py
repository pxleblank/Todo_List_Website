from django.db import models


class Todolist(models.Model):
    user_id = models.ForeignKey('user.User', on_delete=models.CASCADE)
    task = models.TextField(null=False, blank=False)
    state = models.CharField(max_length=64)
