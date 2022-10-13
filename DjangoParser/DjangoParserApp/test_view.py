from django.test import Client
from django.test import TestCase
from faker import Faker
from userapp.models import Applicant


class ViewsTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.fake = Faker()

    def test_statuses(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)

        response = self.client.get('/')
        self.assertTrue('posts' in response.context)

    def test_login_required(self):
        Applicant.objects.create_user(username='test_user', email='test@test.com', password='qwerty123')

        response = self.client.get('/create/')
        self.assertEqual(response.status_code, 302)

        self.client.login(username='test_user', password='qwerty123')

        response = self.client.get('/create/')
        self.assertEqual(response.status_code, 200)

