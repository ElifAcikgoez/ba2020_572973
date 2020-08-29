from django import forms
from .models import *


class TaskForm(forms.ModelForm):
    """
    TaskForm ist der name des Forumulars für die todos und ist ein ModelForm(forms.Modelform). Dem titel
    wird der wert zugewiesen, der im eingabefeld  eingatragen wird. Das eingabefeld bekommt einen Placeholder,
    damit der Nutzer/in auch weiss wo einzutragen ist.
    """
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Hier die Aufgabe eintragen...'}))
   # cover = forms.ImageField(allow_empty_file=True)

    class Meta:
        """
        Das Model Task soll benutzt werden und soll alle felder vom model sichtbar machen.
        """
        model = Task
        fields = '__all__'


class NoteForm(forms.ModelForm):
    """
    NoteForm ist der name des Forumulars für die Notizen und ist ein ModelForm(forms.Modelform)
    """
    class Meta:
        """
         mit  class Meta  sagen wir Django, welches Model benutzt werden soll, um das Formular zu erstellen (model = Note).
         Das Formular soll das textfeld sichtbar machen.
        """

        model = Note
        fields = ('text','post')


class PostForm(forms.ModelForm):
    """
    PostForm ist der name des Forumulars für die Notizen und ist ein ModelForm(forms.Modelform)
    """
    class Meta:
        """
        mit  class Meta  sagen wir Django, welches Model benutzt werden soll, um das Formular zu erstellen (model = Post).
         Das Formular soll das titel eingabefeld und das upload feld für das Bild  sichtbar machen.
        """
        model = Post
        fields = ['title', 'cover', ]

