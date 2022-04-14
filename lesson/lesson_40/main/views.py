from django.shortcuts import render
from .models import Task
from .forms import TaskForm

from rest_framework import viewsets
from .serializers import TaskSerializer


def index(request):
    tasks = Task.objects.all()
    return render(request, 'main/index.html', {
        "title": "Главная страница",
        "header": "Список дел",
        "tasks": tasks,
    })


def contacts(request):
    return render(request, 'main/contacts.html')


def task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
    form = TaskForm()
    context = {
        'form': form
    }
    return render(request, 'main/taskcreate.html', context)


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by('id')
    serializer_class = TaskSerializer
