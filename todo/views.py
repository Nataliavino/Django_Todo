from django.http import HttpResponse
from django.shortcuts import redirect, render

from .models import Task

def addTask(request):
    task = request.POST['task']
    Task.objects.create(task=task)
    return redirect('home')

# def completeTask(request):
#     task = request.POST['task']
#     Task.objects.create(task=task)
#     return redirect('home')

# def deleteTask(request):
#     task = request.POST['task']
#     Task.objects.create(task=task)
#     return redirect('home')

# def updateTask(request):
#     task = request.POST['task']
#     Task.objects.create(task=task)
#     return redirect('home')
