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
    due_date=models.DateField(max_length=200 , null=False)
    dependency=models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title