from .models import Task, Post
from django.forms import ModelForm, TextInput, Textarea


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["title", "description"]
        widgets = {
            "title": TextInput(attrs={
                "class": "form-control",
                "id": "title",
                "aria-describedby": "titleHelp"
            }),
            "description": TextInput(attrs={
                "class": "form-control",
                "id": "description",
                "aria-describedby": "descriptionHelp"
            })
        }


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ["title", "description"]
        widgets = {
            "title": TextInput(attrs={
                "class": "form-control",
                "id": "title",
                "aria-describedby": "titleHelp"
            }),
            "description": Textarea(attrs={
                "class": "form-control",
                "id": "description",
                "aria-describedby": "descriptionHelp"
            })
        }
