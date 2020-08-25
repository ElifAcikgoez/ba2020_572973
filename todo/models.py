from django.db import models
from django.utils import timezone


class Task(models.Model):
	title = models.CharField(max_length=200)
	complete = models.BooleanField(default=False)
	created = models.DateTimeField(auto_now_add=True)


	def __str__(self):
		return self.title

class Note(models.Model):
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
    title = models.TextField()
    cover = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

