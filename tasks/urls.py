from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name="home"),
    path('signup/', views.signup, name="signup"),
    path('task_list/', views.task_list, name="task-list"),
    path('delete/<int:id>/', views.deleteTask, name='delete-task'),
    path('create-task/', views.create_task, name="create-task"),
    path('update/<int:id>/', views.update, name="update-task"),
    path('login/', auth_views.LoginView.as_view(), name='login'),  
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('task_history/', views.task_history, name='task-history')
]
