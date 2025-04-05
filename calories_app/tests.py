from django.test import TestCase
from django.urls import reverse

class MyViewTestCase(TestCase):
    def test_home_view(self):
        """Test if login page returns 200 status"""
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)


class MyViewTestCase1(TestCase):
    def test_home1_view(self):
        """Test if home page returns 200 status"""
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)