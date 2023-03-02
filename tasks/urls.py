from django.urls import path
from .api import TaskAPIList, TaskAPICreate, TaskEdit, CategoryAPICreate, CategoryAPIList, CategoryEdit

urlpatterns = [
    path('api/task_create/', TaskAPICreate.as_view(), name='task_create'),
    path('profile/', TaskAPIList.as_view(), name='profile'),
    path('api/task_edit/<int:pk>/', TaskEdit.as_view(), name='task_edit'),
    path('api/category_create/', CategoryAPICreate.as_view(), name='category_create'),
    path('api/categories/', CategoryAPIList.as_view(), name='categories_list'),
    path('api/category_edit/<str:title>/<int:pk>/', CategoryEdit.as_view(), name='category_edit'),
]