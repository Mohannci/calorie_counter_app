from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from calories_app.models import Food

class MyViewTestCase(TestCase):
    def setUp(self):
        """Set up a test user and food item for views requiring pk"""
        # Create a test user
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        # Create a food item for update_food and delete_food views
        self.food = Food.objects.create(
            person_of=self.user,
            name="Apple",
            calorie=95
        )

    def test_home_view(self):
        """Test if login page returns 200 status"""
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)

    def test_register_view(self):
        """Test if register page returns 200 status"""
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)

    def test_logout_view_unauthenticated(self):
        """Test if logout redirects (302 status) for unauthenticated user"""
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 302)  # Redirect to login page

    def test_add_food_view(self):
        """Test if add food page returns 200 status for authenticated user"""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('add_food'))
        self.assertEqual(response.status_code, 200)

    def test_update_food_view_unauthenticated(self):
        """Test if update food page redirects (302) for unauthenticated user"""
        response = self.client.get(reverse('update_food', args=[self.food.id]))
        self.assertEqual(response.status_code, 302)  # Redirect to login page

    def test_delete_food_view_unauthenticated(self):
        """Test if delete food page redirects (302) for unauthenticated user"""
        response = self.client.get(reverse('delete_food', args=[self.food.id]))
        self.assertEqual(response.status_code, 302)  # Redirect to login page