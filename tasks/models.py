from django.db import models
from users.models import User


class Task(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True, verbose_name='title')
    description = models.CharField(max_length=500, blank=True, null=True, verbose_name='description')
    user = models.ForeignKey(User, verbose_name='task', on_delete=models.CASCADE, related_name='user',
                             blank=True, null=True)
    activity = models.BooleanField(default=False, blank=True, null=True)

    class Meta:
        verbose_name = 'task'
        verbose_name_plural = 'tasks'

    def __str__(self):
        return f'{self.title},{self.description},{self.user}'