from django.db import models
from django.forms import forms


class ToDo(models.Model):
    name = models.CharField(max_length=50)
    # comment = models.CharField(max_length=500)
    write = models.TextField()
    posted_on = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True, auto_now_add=False)
    def __str__(self):
        return (self.name)

