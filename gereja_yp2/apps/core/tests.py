from django.test import TestCase, Client
from django.urls import reverse


class IndexViewTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_index_page_returns_200(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

    def test_home_page_returns_200(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
