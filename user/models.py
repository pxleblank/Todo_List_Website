from django.db import models


class User(models.Model):
    username = models.CharField(max_length=64, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    password = models.CharField(max_length=64, null=False, blank=False)