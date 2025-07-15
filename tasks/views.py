from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse,HttpResponseForbidden
from .models import Tasks, TaskHistory
from .forms import TaskForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


# Create your views here.
def home(request):
    return render(request, "tasks/home.html")


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

            TaskHistory.objects.create(
                user=request.user,
                task=task,
                action='Created',
                note=f"Task '{task.title}' created",
                task_title=task.title,
                task_status=task.status,
                task_priority=task.priority
            )


            messages.success(request, 'Task Added!')
            return redirect('task-list')
    else:
        form = TaskForm()
    
    # Only show tasks belonging to current user in dependencies
    form.fields['dependency'].queryset = Tasks.objects.filter(user=request.user)
    return render(request, 'tasks/create_task.html', {'form': form})

@login_required
def deleteTask(request, id):
    task = get_object_or_404(Tasks, id=id)
    if task.user != request.user:
        return HttpResponseForbidden()
    
    if request.method == 'POST':
        # Store task details BEFORE deleting
        TaskHistory.objects.create(
            user=request.user,
            task=None,  # Task will be deleted
            action='Deleted',
            note=f"Task '{task.title}' deleted",
            task_title=task.title,  # Store name permanently
            task_status=task.status,
            task_priority=task.priority
        )
        
        task.delete()
        messages.success(request, "Task deleted!")
        return redirect('task-list')
    return render(request, 'tasks/confirm_delete.html', {'task': task})

@login_required
def update(request, id):
    task = get_object_or_404(Tasks, id=id)
    if task.user != request.user:
        return HttpResponseForbidden()
    
    if request.method == "POST":
        old_title = task.title
        old_description = task.description
        old_status = task.status
        old_priority = task.priority
        old_due_date = task.due_date

        form = TaskForm(request.POST, instance=task)

        if form.is_valid():
            updated_task = form.save()
            changes = []

            if old_title != updated_task.title:
                changes.append(f"Title: '{old_title}' → '{updated_task.title}'")

            if old_description != updated_task.description:
                changes.append(f"Description updated")

            if old_status != updated_task.status:
                changes.append(f"Status: {old_status} → {updated_task.status}")

            if old_priority != updated_task.priority:
                changes.append(f"Priority: {old_priority} → {updated_task.priority}")

            if old_due_date != updated_task.due_date:
                changes.append(f"Due Date: {old_due_date} → {updated_task.due_date}")
                
            if changes:
                TaskHistory.objects.create(
                    user=request.user,
                    task=task,
                    action='Updated',
                    note='\n'.join(changes),
                    task_title=task.title,
                    task_status=task.status,
                    task_priority=task.priority
                )
                        
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

@login_required
def task_history(request):
    history=TaskHistory.objects.filter(user=request.user).order_by('-action_time')
    return render(request, 'tasks/task_history.html',{'history':history})