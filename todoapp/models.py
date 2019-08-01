from django.db import models
from django.forms import forms


class ToDo(models.Model):
    name = models.CharField(max_length=50)
    # comment = models.CharField(max_length=500)
    write = models.TextField()
    def __str__(self):
        return (self.name)

