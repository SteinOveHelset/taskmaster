from django.shortcuts import render, redirect

from .forms import TaskForm
from .models import Task


def index(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/')
    else:
        form = TaskForm()

    tasks = Task.objects.filter(is_done=False)

    return render(request, 'task/index.html', {
        'form': form,
        'tasks': tasks
    })


def mark_as_done(request, task_id):
    task = Task.objects.get(pk=task_id)
    task.is_done = True
    task.save()

    return redirect('/')


def delete_task(request, task_id):
    task = Task.objects.get(pk=task_id)
    task.delete()

    return redirect('/')