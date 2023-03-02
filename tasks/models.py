from django.db import models
from users.models import User


class Category(models.Model):
    title = models.CharField(max_length=50, blank=True, null=True, verbose_name='title')
    sub_category = models.ForeignKey('self', verbose_name='sub_category', on_delete=models.CASCADE,
                                     related_name='subcategories', blank=True, null=True)
    user = models.ForeignKey(User, verbose_name='user', on_delete=models.CASCADE, related_name='user_category',
                             blank=True, null=True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return f'{self.title}'


class Task(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True, verbose_name='title')
    description = models.CharField(max_length=500, blank=True, null=True, verbose_name='description')
    user = models.ForeignKey(User, verbose_name='task', on_delete=models.CASCADE, related_name='user_tasks',
                             blank=True, null=True)
    activity = models.BooleanField(blank=True, null=True)
    category = models.ForeignKey(Category, verbose_name='category', on_delete=models.CASCADE,
                                 related_name='category_tasks', blank=True, null=True)

    class Meta:
        verbose_name = 'task'
        verbose_name_plural = 'tasks'

    def __str__(self):
        return f'{self.title},{self.description},{self.user},{self.category}'
