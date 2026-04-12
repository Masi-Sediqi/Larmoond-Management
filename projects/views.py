from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import *
from .forms import *


def task_create(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    referer = request.META.get('HTTP_REFERER', '')
    if request.method == 'POST':
        form = ProjectTaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.project = project
            task.created_by = request.user if request.user.is_authenticated else None
            task.save()
            messages.success(request, f"Task '{task.title}' created successfully ✅")
            return redirect(referer)
        else:
            messages.error(request, "Failed to create task ❌")
    else:
        form = ProjectTaskForm()
        tasks = project.tasks.all().order_by('-created_at')

    context = {
        'project':project,
        'task_form':form,
        'tasks':tasks,
    }
    return render(request, 'projects/project-tasks.html', context)
    


def task_update(request, task_id):
    task = get_object_or_404(ProjectTask, id=task_id)
    referer = request.META.get('HTTP_REFERER', '')

    if request.method == 'POST':
        form = ProjectTaskForm(request.POST, instance=task)
        if form.is_valid():
            updated_task = form.save()
            messages.success(request, f"Task '{updated_task.title}' updated successfully ✏️")
        else:
            messages.error(request, "Failed to update task ❌")
    else:
        messages.warning(request, "Invalid task update request ⚠️")

    return redirect(referer)


def task_delete(request, task_id):
    task = get_object_or_404(ProjectTask, id=task_id)
    project_id = task.project.id
    referer = request.META.get('HTTP_REFERER', '')

    if request.method == 'POST':
        task_title = task.title
        task.delete()
        messages.success(request, f"Task '{task_title}' deleted successfully 🗑️")
    else:
        messages.warning(request, "Invalid task delete request ⚠️")

    return redirect(referer)