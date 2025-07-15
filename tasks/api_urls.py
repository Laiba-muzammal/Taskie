from django.urls import path
from .api_views import TaskListCreateAPIView, TaskRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('tasks/', TaskListCreateAPIView.as_view(), name='api-task-list-create'),
    path('tasks/<int:pk>/', TaskRetrieveUpdateDestroyAPIView.as_view(), name='api-task-detail'),
]
