from django.db import models


class Task(models.Model):
    title = models.CharField('Title', max_length=100)
    description = models.TextField('Description', max_length=256)

    def __str__(self):
        return self.title
