from django.shortcuts import redirect
from rest_framework import generics
from rest_framework.mixins import DestroyModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Task
from .serializers import TaskSerializer


class TaskAPICreate(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        return Task.objects.filter(user=user)


class TaskAPIList(generics.ListAPIView):
    """
    TaskAPIList - представление служащее для отображения страницы API со списком всех задач пользователя.
    Его url - /accounts/profile/.
    """

    serializer_class = TaskSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        return Task.objects.filter(user=user)


class TaskEdit(APIView, DestroyModelMixin):
    """
    TaskEdit - представление служащее для отображения страницы API задачи по pk. Его url - api/task_edit/<int:pk>/.
    Где pk - id нужного задания. На этой странице можно удалить выбранное задание и изменить его.
    """
    serializer_class = TaskSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self, request):
        user = self.request.user
        return Task.objects.filter(user=user)

    def get(self, request, pk):
        task = Task.objects.get(id=pk)
        if request.user != task.user:
            raise PermissionError
        else:
            return Response(TaskSerializer(task).data)

    def post(self, request, pk):
        task = Task.objects.get(id=pk)
        data = request.data
        task.title = data.get('title', task.title)
        task.description = data.get('description', task.description)
        task.save()
        return Response(TaskSerializer(task).data)

    def delete(self, request, pk):
        task = Task.objects.get(id=pk)
        task.delete()
        return redirect('/accounts/profile/')
