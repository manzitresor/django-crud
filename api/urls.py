from .views import TaskDetail, TaskListCreate
from rest_framework.urls import path

urlpatterns= [
    path('tasks/', TaskListCreate.as_view(), name='task-list'),
    path('tasks/<int:pk>', TaskDetail.as_view(), name='task-details'),
]