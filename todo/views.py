from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')


def register_user(request):
    return HttpResponse("Register Page")

def logout_user(request):
    return HttpResponse("Logout Page")

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')   # login success
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})

    return render(request, 'login.html')

from django.shortcuts import render, redirect
from .models import Task

def todo_page(request):
    if request.method == "POST":
        title = request.POST.get("title")
        Task.objects.create(title=title)

    tasks = Task.objects.all()
    return render(request, 'todo.html', {'tasks': tasks})


def complete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.completed = True
    task.save()
    return redirect('/todo/')
