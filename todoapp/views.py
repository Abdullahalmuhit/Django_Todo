from django.shortcuts import render, redirect
from .models import ToDo


# Create your views here.
def home(request):
    text = ToDo.objects.all()
    return render(request, 'home.html', {'text': text})


def add_comment(request):
    return render(request, 'index.html')


def create(request):
    print(request.POST)
    name = request.GET['name']
    comment = request.GET['comment']
    store = ToDo(name=name, write=comment)
    store.save()
    return redirect('/')


def delete(request, id):
    text = ToDo.objects.get(pk=id)
    text.delete()
    return redirect('/')


def edit(request, id):
    text = ToDo.objects.get(pk=id)
    return render(request, 'edit.html', {'text': text})


def update(request, id):
    text = ToDo.objects.get(pk=id)
    text.name = request.GET['name']
    text.write = request.GET['comment']
    text.save()
    return redirect("/")
