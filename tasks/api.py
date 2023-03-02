from django.shortcuts import redirect
from rest_framework import generics
from rest_framework.mixins import DestroyModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Task, Category
from .serializers import TaskSerializer, CategorySerializer


class CategoryAPICreate(generics.ListCreateAPIView):
    serializer_class = CategorySerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        return Category.objects.filter(user=user)


class CategoryEdit(APIView, DestroyModelMixin):
    """
    CategoryEdit - представление служащее для отображения страницы API категории по pk.
    Где pk - id нужной категории. На этой странице можно удалить выбранную категорию и изменить её.
    """
    serializer_class = CategorySerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self, request):
        user = self.request.user
        return Category.objects.filter(user=user)

    def get(self, request, title, pk):
        category = Category.objects.filter(title=title).get(id=pk)

        if request.user != category.user:
            raise PermissionError
        else:
            return Response(CategorySerializer(category).data)

    def post(self, request, title, pk):
        category = Category.objects.filter(title=title).get(id=pk)
        data = request.data
        category.title = data.get('title', category.title)
        category.sub_category = Category.objects.get(id=int(data['sub_category']))
        category.save()
        return Response(CategorySerializer(category).data)

    def delete(self, request, title, pk):
        category = Category.objects.filter(title=title).get(id=pk)
        category.delete()
        return redirect('/accounts/profile/')


class CategoryAPIList(generics.ListAPIView):
    """
    CategoryAPIList - представление служащее для отображения страницы API со списком всех категорий пользователя.
    """

    serializer_class = CategorySerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        return Category.objects.filter(user=user)


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
        task.category = Category.objects.get(id=int(data['category']))
        task.save()
        return Response(TaskSerializer(task).data)

    def delete(self, request, pk):
        task = Task.objects.get(id=pk)
        task.delete()
        return redirect('/accounts/profile/')
