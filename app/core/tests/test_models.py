from django.contrib.auth import get_user_model
from django.test import TestCase


class ModelTests(TestCase):
    def test_create_user_with_password(self):
        email = "testuser@example.com"
        password = "testpass"

        user = get_user_model().objects.create_user(email=email, password=password)

        self.assertEqual(email, user.email)
        self.assertTrue(user.check_password(password))

    def test_email_normalization(self):
        password = "testpass"
        emails = (("test@example.com", "test@example.com"), ("Test@Example.Com", "Test@example.com"))

        for email, expected_email in emails:
            user = get_user_model().objects.create_user(email=email, password=password)
            self.assertEqual(user.email, expected_email)

    def test_empty_email(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(email="", password="testpass")
