from django.contrib.auth import get_user_model
from django.test import TestCase


class ModelTests(TestCase):
    def test_create_user_with_password(self):
        email = "testuser@example.com"
        password = "testpass"

        user = get_user_model().objects.create_user(email=email, password=password)

        self.assertEqual(email, user.email)
        self.assertTrue(user.check_password(password))
