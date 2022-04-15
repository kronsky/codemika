from django.shortcuts import render
from .models import Task, Post
from .forms import TaskForm, PostForm

from rest_framework import viewsets
from .serializers import TaskSerializer, PostSerializer


def index(request):
    return render(request, 'main/index.html')


def tasklist(request):
    tasks = Task.objects.all()
    return render(request, 'main/tasklist.html', {
        "title": "Главная страница",
        "header": "Список дел",
        "tasks": tasks,
    })


def taskcreate(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
    form = TaskForm()
    context = {
        'form': form
    }
    return render(request, 'main/taskcreate.html', context)


def postlist(request):
    posts = Post.objects.all()
    return render(request, 'main/postlist.html', {
        "title": "Статьи",
        "header": "Статьи",
        "posts": posts,
    })


def postcreate(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
    form = PostForm()
    context = {
        'form': form
    }
    return render(request, 'main/postcreate.html', context)


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by('id')
    serializer_class = TaskSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('id')
    serializer_class = PostSerializer
