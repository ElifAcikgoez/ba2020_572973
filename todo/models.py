from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.db import models
from django.utils import timezone


# Django-Model: eine Vorlage , nach welcher wir zukünftig unsere objekte erstellen können.

class Task(models.Model):
    """
    Vorlage für die Todos, nach welcher die Taskobjekte erstellt werden.
    """
    title = models.CharField(max_length=200)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    cover = models.ImageField(upload_to='images/',blank=True,)

    def __str__(self):
        return self.title


class Note(models.Model):
    """
    Vorlage für die Notizen, nach welcher die Noteobjekte erstellt werden.
    """
    post = models.ForeignKey('todo.Task', on_delete=models.CASCADE, related_name='notes')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_note = True
        self.save()

    def __str__(self):
        return self.text


class Post(models.Model):
    """
    Vorlage für die Bildposts, nach welcher die objekte erstellt werden.

    """
    title = models.TextField()
    cover = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.title
