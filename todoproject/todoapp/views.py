from django.shortcuts import render, redirect
from .models import Task
from .forms import TodoForm

def add(request):
    task1 = Task.objects.all()
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    else:
        form = TodoForm()

    return render(request, 'home.html', {'task1': task1, 'form': form})

def delete(request, taskid):
    task = Task.objects.get(id=taskid)
    if request.method == 'POST':
        task.delete()
        return redirect('/')
    return render(request, 'delete.html', {'task': task})

def update(request, id):
    task = Task.objects.get(id=id)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = TodoForm(instance=task)

    return render(request, 'edit.html', {'form': form, 'task': task})
