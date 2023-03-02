import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

from rest_framework.test import APITestCase


class TestUser(APITestCase):

    def test_create_account(self):
        response = self.client.get('http://127.0.0.1:8000/users/api/register/')
        self.assertEqual(response.status_code, 200)