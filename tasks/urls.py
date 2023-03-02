from django.urls import path
from .api import TaskAPIList, TaskAPICreate, TaskEdit

urlpatterns = [
    path('api/task_create/', TaskAPICreate.as_view(), name='task_create'),
    path('profile/', TaskAPIList.as_view(), name='profile'),
    path('api/task_edit/<int:pk>/', TaskEdit.as_view(), name='task_edit'),
]