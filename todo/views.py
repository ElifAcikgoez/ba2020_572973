
from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from .models import  Task
from django.contrib.auth.decorators import login_required
@login_required
def index(request):
	tasks = Task.objects.all()

	form = TaskForm()

	if request.method =='POST':
		form = TaskForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('/')


	context = {'tasks':tasks, 'form':form}
	return render(request, 'todo/list.html', context)

def updateTask(request, pk):
	task = Task.objects.get(id=pk)

	form = TaskForm(instance=task)

	if request.method == 'POST':
		form = TaskForm(request.POST, instance=task)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form':form}

	return render(request, 'todo/update_task.html', context)

def deleteTask(request, pk):
	item = Task.objects.get(id=pk)

	if request.method == 'POST':
		item.delete()
		return redirect('/')

	context = {'item':item}
	return render(request, 'todo/delete.html', context)

def completeTodo(request, todo_id):
    todo = Task.objects.get(pk=todo_id)
    todo.complete = True
    todo.save()

    return redirect('list')

def deletecompleted(request):
	Task.objects.filter(complete__exact=True).delete()

	return redirect('list')

def deleteall(request):
    Task.objects.all().delete()

    return redirect('list')


def details(request, id):
    todo = Task.objects.get(id=id)

    context = {
        'todo':todo
    }
    return render(request, 'update_task.html', context)

def add_note_to_post(request, pk):
    post = get_object_or_404(Task, pk=pk)
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.post = post
            note.save()
            return redirect('list')
    else:
        form = NoteForm()
    return render(request, 'todo/add_note_to_post.html', {'form': form})