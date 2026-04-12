from django.urls import path
from . import views

app_name = 'projects'

urlpatterns = [
    path('projects/<int:project_id>/tasks/create/', views.task_create, name='task_create'),
    path('tasks/<int:task_id>/update/', views.task_update, name='task_update'),
    path('tasks/<int:task_id>/delete/', views.task_delete, name='task_delete'),
]