from django.contrib import messages
from django.core.files.uploadhandler import FileUploadHandler
from django.forms import modelform_factory
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
#from .models import Post
from .forms import *
from .models import Task
from django.contrib.auth.decorators import login_required

"""
In der View schreiben wir die Logik der Anwendung. So werden Informationen aus dem Model
 abgefragt und diese werden an ein Template weitergegeben.
"""

@login_required
def index(request):
    """
    Diese Funktion sorgt dafür, dass die eingetragenen todos gespeichert werden und in der Liste erscheinen.
    Es wird geprüft , ob die request methode die der Client getätigt hat ein POST-Request ist. Wenn ja,
    dann wird der TaskForm als parameter der request.POST übergeben. Wenn das formular (if form.is_valid)
    true (gültig) ist, wird es gespeichert und das Template (todo/list.html) wird zu einer fertigen
    HTML-Seite zusammengesetzt("gerendert").

    :param request: HTTP request des Clients
    :type request:str
    :return:Die komplette todo Liste
    :rtype:html
    """
    tasks = Task.objects.all()
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/')

    context = {'tasks': tasks, 'form': form}
    return render(request, 'todo/list.html', context)


@login_required
def updateTask(request, pk):
    """
    Die Funktion updateTask erstellt die die HTML seite für den gewünschten todo , den man bearbeiten/updaten möchte.

    :param request: HTTP-Request des Clients
    :type request: str
    :param pk: Primary-key des zu bearbeitenden toDos
    :type pk: int
    :return: HTML Seite wo man den gewünschten todo bearbeiten und abspeichern kann
    :rtype:html
    """
    task = Task.objects.get(id=pk)
    """var: task : Das genaue To-do was bearbeitet werden soll mit dem index des Primary-keys."""
    form = TaskForm(instance=task)
    """var: form : Formular für das zu bearbeitende to-do. """
    if request.method == 'POST':
        form = TaskForm(request.POST, request.FILES, instance=task)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')

    context = {'form': form}

    return render(request, 'todo/update_task.html', context)
@login_required
def updatenotiz(request, pk):
    """
    Die Funktion updatenotiz erstellt die die HTML seite für den gewünschten todo , den man eine notiz hinzufügen möchte.

    :param request: HTTP-Request des Clients
    :type request: str
    :param pk: Primary-key des  toDos wo man die notiz hinzufügen möchte
    :type pk: int
    :return: HTML Seite wo man den gewünschten todo den notiz text eingeben kann
    :rtype:html
    """
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, request.FILES, instance=task)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')

    context = {'form': form}

    return render(request, 'todo/update_note.html', context)

@login_required
def deleteTask(request, pk):
    """
    Diese Funktion ermöglicht es, den gewünschten  todo zu löschen.

    :param request: HTTP-request des Clients
    :type request:str
    :param pk: Primary-key des zu löschenden toDos
    :type pk:int
    :return:HTML Seite wo man den gewünschten todo löschen  kann
    :rtype:html
    """
    item = Task.objects.get(id=pk)

    if request.method == 'POST':
        item.delete()
        return redirect('/')

    context = {'item': item}
    return render(request, 'todo/delete.html', context)


@login_required
def completeTodo(request, todo_id):
    """
    Diese Funktion setzt den complete Wert aus dem Model des todos ,welches default false ist, auf true.
    :param request: HTTP-Request des Clients
    :type request:str
    :param todo_id: Die id von dem todo welches auf erledigt gesetzt sein soll
    :type todo_id:int
    :return:zurück zur list url
    :rtype:str
    """
    todo = Task.objects.get(pk=todo_id)
    todo.complete = True
    todo.save()

    return redirect('list')


@login_required
def deletecompleted(request):
    """
    Diese Funktion löscht die erledigten todos.

    :param request:HTTP-request des client
    :type request:str
    :return:wieder auf die todo-liste
    :rtype:str
    """
    Task.objects.filter(complete__exact=True).delete()

    return redirect('list')


@login_required
def deleteall(request):
    """
    Diese funktion löscht alle eingetragenen todos.

    :param request: HTTP-Request des client
    :type request: str
    :return: Man wird wieder  auf die "start seite"(todo-liste) geleitet/redirected
    :rtype: str
    """
    Task.objects.all().delete()

    return redirect('list')


@login_required
def details(request, id):
    todo = Task.objects.get(id=id)

    context = {
        'todo': todo
    }
    return render(request, 'update_task.html', context)

@login_required
def searchdata(request):
    """
    Mit dieser Funktion kann man nach beliebigen wörtern suchen und den passenden todo dazu sich anzeigen lassen.
    Die Funktion sucht in dem todo-titel nach dem gesuchten wort.
    """
    q = request.GET['query']
    mydictionary = {
        "tasks" : Task.objects.filter(title__contains=q)
    }
    return render(request,'todo/index.html',context=mydictionary)

#@login_required
#def add_note_to_post(request, pk):
 #   """
  #  Diese Funktion fügt zu jedem todo eine notiz hinzu.
#
  #  :var post: soll entweder
 #   :param request: HTTP-request des client
   # :type request: str
    #:param pk: Primary Key des todos
    #:type pk: int
    #:return: Gibt die HTML seite zurück , wo man die Noitz zu dem todo mit dem bestimmten Primary-key eintragen kann.

   # """
    #post = get_object_or_404(Task, pk=pk)
    #if request.method == "POST":
     #   form = NoteForm(request.POST)
      #  if form.is_valid():
       #     note = form.save(commit=False)
        #    note.post = post

#            note.save()
 #           return redirect('list')
  #  else:
   #     form = NoteForm()
    #return render(request, 'todo/add_note_to_post.html', {'form': form})


#def post_list(request):
 #   posts = Post.objects.all()
  #  return render(request, 'post_list.html', {
   #     'posts': posts
    #})


#def delete_post(request, pk):
 #   if request.method == 'POST':
  #      post = Post.objects.get(pk=pk)
   #     post.delete()
    #return redirect('post_list')


#class CreatePostView(CreateView):
 #   model = Post
  #  form_class = PostForm
   # template_name = 'post.html'
    #success_url = reverse_lazy('list')
