from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse,HttpResponseForbidden
from .models import Tasks
from .forms import TaskForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

# Create your views here.
def home(request):
    return render(request, "tasks/home.html")
# views.py

@login_required
def task_list(request):
    # Get tasks for current user and separate by status
    tasks = Tasks.objects.filter(user=request.user)
    pending_tasks = tasks.filter(status='Pending')
    in_progress_tasks = tasks.filter(status='In Progress')
    completed_tasks = tasks.filter(status='Completed')
    
    return render(request, 'tasks/task_list.html', {
        'pending_tasks': pending_tasks,
        'in_progress_tasks': in_progress_tasks,
        'completed_tasks': completed_tasks,
    })

@login_required
def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            messages.success(request, 'Task Added!')
            return redirect('task-list')
    else:
        form = TaskForm()
    
    # Only show tasks belonging to current user in dependencies
    form.fields['dependency'].queryset = Tasks.objects.filter(user=request.user)
    return render(request, 'tasks/create_task.html', {'form': form})


@login_required
def deleteTask(request,id):
    task=get_object_or_404(Tasks,id=id)
    if task.user != request.user:
        return HttpResponseForbidden()
    if request.method=='POST':
        task.delete()
        messages.success(request,"Task deleted!")
        return redirect('task-list')
    return render(request, 'tasks/confirm_delete.html', {'task': task})


@login_required
def update(request, id):
    task = get_object_or_404(Tasks, id=id)
    if task.user != request.user:
        return HttpResponseForbidden()
    
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, "Task updated!")
            return redirect('task-list')
    else:
        form = TaskForm(instance=task)
    
    # Filter dependencies to show only current user's tasks
    form.fields['dependency'].queryset = Tasks.objects.filter(user=request.user).exclude(id=task.id)
    
    return render(request, 'tasks/update_task.html', {'form': form, 'task': task})

def signup(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request, user)  # auto login after signup
            return redirect('task-list')
    else:
        form = UserCreationForm()
    return render(request, 'tasks/signup.html', {'form': form})
