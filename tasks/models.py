from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Tasks(models.Model):

    PRIORITY_CHOICES = [
    ('Low', 'Low'),
    ('Medium', 'Medium'),
    ('High', 'High'),
    ]

    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title=models.CharField(max_length=200 , null=True)
    description = models.CharField(max_length=2000, null=False, default="No description")
    priority=models.CharField(max_length=10 , choices=PRIORITY_CHOICES, null=True)
    status=models.CharField(max_length=15 , choices=STATUS_CHOICES,default='Pending' )
    due_date=models.DateField(max_length=200 , null=True, blank=True)
    dependency=models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
from django.db import models
from django.contrib.auth.models import User

from django.db import models
from django.contrib.auth.models import User

class TaskHistory(models.Model):
    ACTION_CHOICES = [
        ('Created', 'Created'),
        ('Updated', 'Updated'),
        ('Deleted', 'Deleted'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='task_histories')
    task = models.ForeignKey('Tasks', on_delete=models.SET_NULL, null=True, blank=True)
    action = models.CharField(max_length=50, choices=ACTION_CHOICES)
    note = models.TextField(blank=True)
    action_time = models.DateTimeField(auto_now_add=True)
    task_title = models.CharField(max_length=200, default='(No title)')
    task_status = models.CharField(max_length=15, default='Pending')
    task_priority = models.CharField(max_length=10, default='Medium')
    
    def __str__(self):
        return f"{self.action} - {self.task_title} ({self.action_time})"