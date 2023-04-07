from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse


# Create your tests here.
class UserTestCase(TestCase):

    def setUp(self) -> None:
        self.URL = 'http://127.0.0.1:8000/'
        self.credentials = {
            'username': 'test_user',
            'password': 'admin'
        }
        self.user = User.objects.create_user(**self.credentials)

    def test_user_has_username(self):
        self.assertEqual(self.user.username, 'test_user')

    def test_server_connection(self):
        # перевірка запуск сервера
        response = self.client.get(reverse('home'))
        response2 = self.client.get(f'{self.URL}login/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response2.status_code, 200)

    def test_login_user(self):
        response = self.client.post(self.URL + 'login/', self.credentials, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertRedirects(response, reverse('home'))

    # def test_login_user(self):
    #     user = User.objects.get(username='test_user')
    #     self.assertTrue(user.check_password('admin'))
