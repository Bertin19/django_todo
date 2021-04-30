from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm

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


# Create
def todo_create(request):
    # if POST-request sent then form will be populated
    form = TodoForm(request.POST or None)

    if form.is_valid():
        print(form.cleaned_data)
        # create a todo object
        form.save()
        return redirect('/')
    context = {'form': form}
    return render(request, "todo/todo_create.html", context)
        
