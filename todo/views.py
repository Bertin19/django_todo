from django.http import HttpResponse
from django.shortcuts import render
from .models import Todo

# Create your views here.

# CRUD - Create, Retrieve, Update, Delete, List

# List
def todo_list(request):
    todos = Todo.objects.all()
    print("Test ", todos)
    context = {
        "todo_list": todos
    }
    return render(request, "todo/todo_list.html", context)

# Retrieve
def todo_detail(request, id):
    todo = Todo.objects.get(id=id)
    context = {
        'todo': todo
    }
    return render(request, "todo/todo_detail.html", context)
