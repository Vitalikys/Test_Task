from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse


# Create your tests here.
class CsvGeneratorTestCase(TestCase):

    def setUp(self) -> None:
        self.baseURL = 'http://127.0.0.1:8000/'
        self.credentials = {
            'username': 'test_user',
            'password': 'admin'
        }
        self.user = User.objects.create_user(**self.credentials)

    def test_create_schema(self):
        url = self.baseURL + 'csv/add_schema/'
