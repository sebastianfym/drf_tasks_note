import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
from rest_framework.test import APIRequestFactory, RequestsClient, APITestCase, force_authenticate, APIClient
from users.models import User


class TaskTest(APITestCase):
    user = User.objects.get(username='test')
    client = APIClient()

    def test_create_get(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get('http://127.0.0.1:8000/tasks/api/task_create/')
        self.assertEqual(response.status_code, 200)

    def test_create_post(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.post('http://127.0.0.1:8000/tasks/api/task_create/', json={
            "title": 'TestTitle',
            "description": 'TestDescription',
            'user': self.user,
            'activity': True
        })
        self.assertEqual(response.status_code, 201)

    def test_profile_view(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get('http://127.0.0.1:8000/accounts/profile/')
        self.assertEqual(response.status_code, 200)

    def test_edit_get(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get('http://127.0.0.1:8000/tasks/api/task_edit/2/')
        self.assertEqual(response.status_code, 200)
