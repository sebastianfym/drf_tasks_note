from django.urls import path, include
from .api import RegisterUserAPI

urlpatterns = [
    path('api/register/', RegisterUserAPI.as_view(), name='register'),
    path('api/drf-auth/', include('rest_framework.urls')),
]