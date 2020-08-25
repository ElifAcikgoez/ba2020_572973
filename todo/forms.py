from django import forms
from .models import *


class TaskForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Hier die Aufgabe eintragen...'}))

    class Meta:
        model = Task
        fields = '__all__'


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ('text',)

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'cover',]