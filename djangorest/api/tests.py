from django.test import TestCase
from .models import User
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse

class ModelTestCase(TestCase):
    """This class defines the test suite for the user model."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.user_name = "Mad Scientist"
        self.user = User(name=self.user_name)

    def test_model_can_create_a_userlist(self):
        """Test the user model can create a user."""
        old_count = User.objects.count()
        self.user.save()
        new_count = User.objects.count()
        self.assertNotEqual(old_count, new_count)


class ViewTestCase(TestCase):
    """Test suite for the api views."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.client = APIClient()
        self.user_data = {'name': 'Alchemist'}
        self.response = self.client.post(
            reverse('create'),
            self.user_data,
            format="json")

    def test_api_can_create_a_user(self):
        """Test the api has user creation capability."""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)